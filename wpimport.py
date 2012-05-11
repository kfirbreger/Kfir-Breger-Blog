#!/usr/bin/env python

from xml.etree.ElementTree import ElementTree
from BeautifulSoup import BeautifulSoup
import html2text
import sys
import re
import codecs
import os
import sys
from urlparse import urlparse, urljoin
from urllib import urlretrieve


# Saving dir
base_dir = 'export' # Change to content for live

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '-', value))
    return value

def prepareBody(body):
    img_srcs = []
    if body is not None:
        try:
            soup = BeautifulSoup(body)
            img_tags = soup.findAll('img')
            for img in img_tags:
                img_srcs.append(img['src'])
        except:
            print "could not parse html: " + body
    return img_srcs

def main(filename):
    imgs_dir=os.path.normpath(base_dir + '/images')
    #target_file=os.path.normpath(target_dir+'/'+filename)
    
    # Adding namespaces
    namespaces = {
        '':'', #this is the default namespace
        'excerpt':"{http://wordpress.org/export/1.1/excerpt/}",
        'content':"{http://purl.org/rss/1.0/modules/content/}",
        'wfw':"{http://wellformedweb.org/CommentAPI/}",
        'dc':"{http://purl.org/dc/elements/1.1/}",
        'wp':"{http://wordpress.org/export/1.1/}",
        'atom':"{http://www.w3.org/2005/Atom}"
    }
    
    def determineSuffix():
        """
        Checks the config to see which suffix to use.
        If suffix plugin is present and set to convert markdown to html, the FIRST encountered markdown suffix will be used.
        Otherwise the suffix will be 'html'.
        """
        suffix = 'md' # assume no suffix plugin
        return suffix
            
    def parseHeader():
        tags = []
        joiner = ', '
        for tag in item.findall('category'):
            if "domain" in tag.attrib:
                t = unicode(tag.text)
                tags.append(t)
        # This will be put in the header
        title = unicode(item.find('title').text)
        header = u"Title:" + title + u"\nDate: " + item.find(namespaces['wp'] + 'post_date').text + u"\nTags: " + joiner.join(tags) + "\n\n"
        return {'title': title, 'data': header}
    def parseContent():
        # Retriving post
        content = unicode(item.find(namespaces["content"] + "encoded").text)
        replace_images = {}
        # Fetching Images
        imgs = prepareBody(content)
        if imgs:
            for img in imgs:
                try:
                    img_filename = img.rpartition('/')[2]
                    img_filename = img_filename.rpartition('.')
                    filename = imgs_dir + '/' + slugify(img_filename[0]) + '.' + img_filename[2]
                    # print img.decode('utf-8'), "->", filename
                    urlretrieve(img.decode('utf-8'), filename)
                    replace_images[str(img)] = str(filename)
                except:
                    print "\n unable to download " + img.decode('utf-8')
                    print sys.exc_info()[1]
                
        # Returning Markdown
        try:
            md = html2text.html2text(content)
            # replacing images links
            for img_url, img_file in replace_images.items():
                md = md.replace(img_url, img_file)
        except:
            md = None
        return md
    
    def buidlPost():
        """
        Builds the header the content of the post and saves them in a dictionary.
        The header contains a dictionary with all the header information. The content contains the actual post
        """
        post = {}
        post['header'] = parseHeader()
        post['content'] = parseContent()
        # Returning the post
        return post
    
    def savePost(post):
        """
        Creates a file with the post. 
        """
        filename = unicode(post['header']['title'])
        filename = base_dir + '/' + slugify(filename) + '.' + suffix
        f = codecs.open(filename, encoding='utf-8', mode='w+')
        f.write(post['header']['data'])
        if post['content']:
            f.write(post['content'])
        else:
            print "Failed to parse content of " + post['header']['title']
            f.write('')
        f.close()
    
    # Loading the xml
    try:
        f = open(filename)
    except:
        print "Cannont open file"
        sys.exit()
    try:
        tree = ElementTree()
        root = tree.parse(f)
    except:
        print "Failed to parse xml file"
        sys.exit()
    # Setting the file suffix
    suffix = determineSuffix();    
    # Iterating over items
    for item in root.iter('item'):
        post = buidlPost()
        savePost(post)

if __name__ == '__main__':
    main('wordpress.xml') # @TODO Add paramter wordpress xml name