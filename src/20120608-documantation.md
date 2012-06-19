Title: Going Static
Date: 2012-06-08
tags: pelican, python

All the cool ids are doing it!
For a good reason. I decided a while a go to turn off comments in my blog(A whole other discussion). Once comments are out there is no real reason to use a database for the blog since the posts pages are pretty static. Also, I am trying to minimize the amount of php I use. Moving away from wordpress was high on that list. So I looked around for a static generator.

## The options
The first name I came across is [Jekyll](http://jekyllrb.com/). Developed by [github](http://github.com), it is a very popular engine. I, however decided to skip it as it seems rather strict in how it does things, and what it can do, and because it was in ruby. I have nothing against ruby, but I prefer not to learn a new programming language at the moment. The next candidate was [hyde](https://github.com/hyde/hyde) which is a static website generator written in python, originally developed as a port of Jekyll, it is quite different. Hyde lookd more flexible and it was written in a language I know and love. So I picked it. For a really good, though a bit old,  comparison of the two check out [Philip Mat's blog](http://philipm.at/2011/0507/) and [Distractable](http://www.distractable.net/tech/static-site-generators-jekyll-vs-hyde).

## Going Hyde
So Hyde it was, on with the show. Documentation was somewhat missing, but at this point it was not really a problem. This being python, getting started is a breeze.

### Setup
Installing hyde is as easy as

    pip install hyde

I highly recommend you use a virtualenv.

###Adding preprocessing
Hyde uses preprocesses to work with your content. This is a very powerful features and one of the reason I wanted to work with hyde. Since you can write your own you can pretty much do anything with your content.
### Extensions
Hyde is by default in your (virtualenv) site-packages. To add an extension, add the extension file to the lib/python2.7/site-packages/hyde/ext/plugins/ folder.

#### Markdown
Hyde by supports markdown out of the box. However it does not support changing the extension. that is, if your file's extension is .md, Hyde will deploy it as a .hd file, even though the content has been alterd to html. The [suffix extension](https://github.com/lepture/hyde.ext/blob/master/plugins/suffix.py) converts file suffixes. It is configurable through the site.yml

### Content
Hyde takes your content and generates static html from it. In this section I will try, to the best of my knowledge to explain how the generation of content works. 
#### Location
Content goes into the content folder. Generally speaking hyde will, unless otherwise instructed, render each file in the content folder as its own html page. Hyde emulates the folder construction in the content folder for the actual website. So, for instance, if your content folder looks like this:

    -content
    --about.md
    --blog
    ---posts.md
    ---2012
    ----myfirstpost.md


Then the generated website will look like this:

    -www.example.com
    --about.html (www.example.com/about.html)
    --blog
    ---posts.html
    ---2012
    ----myfirstpost.html (www.example.com/blog/2012/myfirstpost.html)

This makes it quite easy to determine the paths inside your website

#### Anatomy of a content file
A content file should start with a YAML Front Matter[^2]. This is used to add some metadata to the post. An example is given here:

    ---
    title: Test post html
    description: A test post for hyde
    created: !!timestamp '2012-01-01 10:00:00'
    tags:
        - ideas
        - thoughts
    ---
 
As you can see the YAML Front Matter starts and ends with ---. In between the title, description, created date and tags are given. I am not aware of any other metadata available. This part is not required. I need to test what the defaults are.

After the YAML Front Matter heading, the actual post can be written. Hyde supports markdown[^3], which is quite easy to use.

### Templating
Hyde uses the [jinja2](http://jinja.pocoo.org) templating engine. It is quite similar to Django's templating engine[^1].

#### Choosing a template
As far as I can tell hyde chooses which template file to use following these rules:

1. If the content file has an __extends__ attribute in the yaml head, use that template
2. Otherwise, if there is a meta.yaml in the folder with an __extends__ attribute, use that
3. Move folders up until you find a meta.yaml and if it has an __extends__ use that.
4. If no template file is found, the file is not rendered in a template and is simply copied over to the deploy folder.

#### Mark
Hyde uses the mark tag to mark certain pieces that will be used elsewhere. The official list should eventually be available in the [markrefer](http://hyde.github.com/templates/markrefer.html) page of github. However at the moment this page contains no data. Here is a, probably incomplete list, of marks

* image - Used for images
* excerpt - Used as teasers in blog

Marks are used like jinja macros with the - sign for start and end, i.e.

    {% mark image -%}
    ![Airport]([[!!images/airport.png]])
    {%- endmark %}

For an image mark

####Creating  a list
There are several lists which any blog needs to generate. Some of these lists will be used to create pages just for them. However since the documentation was so lacking I was unable to find a way to do this the way I wanted

###Giving up
At was at this point after investing hours, that I gave up on hyde. It looks great, and I am sure that it can do what I want. However lack of documentation makes it really hard to work with. I decided this already took to much of my time and so went to look elsewhere.

##Blacksmith
It was time to try something completely different. [Blacksmith](http://blog.nodejitsu.com/introducing-blacksmith) is a node.js based static engine create by [nodejitsu](http://nodejitsu.com). It all looked very promising, until I saw that each post needs to have its own directory and that it has 1 file for the content and a json file for the header. For me that was just to much.

##Pelican
I was close to give up and stick to wordpress when I can across [Pelican](http://pelican.readthedocs.org/en/latest/). Written in python, and with great documentation, it was just what I needed. The docs are, in fact, so good that I really don't need to write any guide or about how I finally made the change. I will tell you this tough, it took me all of 3 hours, including importing the content from wordpress. Pelican is elegant, easy to use, well documented and it renders the markdown files quite fast. All I was looking for.


[^1]: Jinja2 can in fact be used in Django as well.
[^2]: Jekyll terminology. I do not know if hyde has its own term for this. The idea is the same, though the supported syntax is, as of writing, not.
[^3]: Markdown was introduced by John Gruber for the exact purpose of simplifying writing for the web. Learn more at [daring fireball.net](http://daringfireball.net/projects/markdown/)
