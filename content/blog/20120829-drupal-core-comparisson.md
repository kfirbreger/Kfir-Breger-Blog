Title: Drupal Core Comparison
Date: 2012-08-29
Tags: drupal, programming, unix

Drupal strongly discourages core hacks. Unfortunately not everybody follows this guideline. It will happen on occasion(more often than I would like) that you get to work on a project that needs a core update, and has undocumented core hacks. This of course poses a problem.

The solution to this bad situation is to find what the core hacks are, analyse them, to see if they are still needed[^1], then create a patch for them. Once the patch is made, update the core and reapply, if possible. I recommend creating a patch per file as it makes it easier to get over problems with patching.

##Finding the differences
The first step would be to find out which version of drupal the current installation is using. [Download that version](http://drupal.org/node/3060/release) and and put it somewhere on your local system. In the code example here I will use the directory names core and project to note the downloaded core version, and the project version directories respectively. If a special drupal release is used, such as pressflow, you will need to download that releases matching version and not drupal default release. The first order of business is to identify all the files that are different between core and project. Inverted grep is used to remove from the output all the files that are in project but not in core as we are not interested in those.

	diff -wBrq core project | grep -v "Only in"

Comparing two directories, ignoring white spaces and empty lines, showing only the files that differ, working recursively. If you want to save the differences you can push the output to a file. I highly recommend doing that for later reference.

##Creating the patches
Now that the files that differ are know a per file check is needed. Check each file, and create a patch. If you do not know how to create patches	 with diff, this [10 minute guide](http://jungels.net/articles/diff-patch-ten-minutes.html) is helpful. If you have saved the output of the previous diff in a file you can use the following python script to create a patch per file[^2].

	import sys
	import os
	
	f = open(sys.argv[1])
	for line in f:
    	data = line.split()
    	pfname = data[1].split('/')[-1]
    	cmd = 'diff -uBw ' + data[1] + ' ' + data[3] + ' > patches/' + pfname + '.patch'
    	print cmd
    	os.system(cmd)
	f.close()

It assumes there is a directory called patches to save all the patch files. You call it giving the diff file as arg:

	python diffscript.py total_diff_file.txt

In the patches directory there will now be a file name file.patch for each file that differs. It is of course also possible to just create one big patch file using diff. If you are interested in doing that you can use the following command:

	diff -wBur core project > core_project_diff.patch

##Analysis and Applying
This step cannot be automated. You need to check each patch file to see what are the differences, and see if they need to be reapplied. If they do, save the patch file, otherwise the patch file can be removed. Once all the hacks have been identified and noted, the core can be updated.

The core is now at the wanted version and it is time to reapply the patch. Though you could just use the patch command, a check is in order to make sure that the patches will be applied where they are expected.

[^1]: If you have the time, also see if you can solve the problem in a non core hack manner.

[^2]: This script is in no way safe or robust. It is a quick and simple example. Feel free to create better/different version of it. 