Title: Views 2 integration and custom handlers in Drupal 6
Date: 2010-02-10 19:32:46
Tags: drupal, programming, views2, web, work

As part of a large scale project at work, I needed to create an integration
between views and a module I was writing. For it to function properly, a
custom handler was also needed. Unfortunately there was very little
information to be found about how this must be done. The integration process
is not that complex, and it can be understood from the code sample given in
the views 2 docs. A custom handler however proved to be somewhat more elusive.
To do my part in helping clear some of it up, I will give a simplified, step
by step, guide how I have solved this. I am by no means an expert when it
comes to views, and it is possible that there are better solutions out there.
I, however, was unable to find them.

### The Setup

As a simplified version of the actual module we will imagine a module that is
intended to collect messages generated by users actions. The module will then
show actions generated by your "friends". Think something like Facebooks news
feed. How you befriend someone or how the messages are generated are not
important for this guide, so just assume that it all goes well. When it does
pay a roll, I will give all the needed information.

Our module is called buzz.

### Data Structure

The messages have a few pre-set forms (think facebook's news feed again) with
a few values that change. For instance

username has added a photo to his profile

To minimize the amount of data in the database we will define table that
contains the text of he message, and which arguments are expected. In this
way, the actual message just needs to save the message type and the arguments,
preventing repeating the whole message. It also gives more flexibility in
changing the form of the message to all messages at once.

The following schema

[![Schema describing the database](/images/buzz-db-schema-300x213.png)](/01/buzz-db-schema.png)

represent how the data is being saved into the database. The database tables
are built using hook_schema() and hook_install(). The messages are entered
into the database via an API that the module offers. The specifics are not
important for this post, though if there will be demand for it I will post
about it.

### Views Integration

There are quite a few advantages to integrate your module's data module with
views.

  * Flexibility in representation of data
  * Easier for other people to work with your module

To name two major ones. Views integration is done through the use of the
hook_views_data(). What this hook does basically is tell views all that it
needs to know in order to be able to work with your data model. I'll give the
implementation first, followed by an explaintion.

    
    
    <?php
    function buzz_views_data() {
            $data = array();
    	$data['buzz_message_types'] = array(
    		'table' => array(
    			'group' => t('Buzz'),
    			'join' => array(
    				'buzz_messages' => array(
    					'left_field' => 'msg_type_id',
    					'field' => 'id',
    				),
    			),
    		),
    		'id' => array(
    			'title' => t('Message type ID'),
    			'help' => t('ID of the message type.'),
    			'field' => array(
    				'handler' => 'views_handler_field',
    				'click sortable' => TRUE,
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_string',
    			),
    			'argument' => array(
    				'handler' => 'views_handler_argument_string',
    			),
    		),
    		'args_type' => array(
    			'title' => t('Arguments type'),
    			'help' => t('What type of arguments this message type expect.'),
    			'field' => array(
    				'handler' => 'views_handler_field',
    				'click sortable' => TRUE,
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_string',
    			),
    			'argument' => array(
    				'handler' => 'views_handler_argument_string',
    			),
    		),
    		'txt' => array(
    			'title' => t('Message base text'),
    			'help' => t('Text of the message type, with the wildcards not filled'),
    			'field' => array(
    				'handler' => 'views_handler_field',
    				'click sortable' => TRUE,
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_string',
    			),
    			'argument' => array(
    				'handler' => 'views_handler_argument_string',
    			),
    		),
    	);
    	$data['buzz_messages'] = array(
    		'table' => array(
    			'group' => t('Buzz'),
    			'base' => array(
    				'field' => 'id',
    				'title' => t('Messages'),
    				'help' => t('Messages table'),
    			),
    			'join' => array(
    				'users' => array(
    					'left_table' => 'buzz_message_usr',
    					'left_field' => 'msg_id',
    					'field' => 'id',
    				),
    			),
    		),
    		'message' => array(
    			'real_field' => FALSE,
    			'title' => t('The message'),
    			'help' => t('The composed message, built from the message type and the arguments.'),
    			'field' => array(
    				'handler' => 'buzz_handler_field_message',
    				'click sortable' => TRUE,
    			),
    		),
    		'id' => array(
    			'title' => t('Message ID'),
    			'help' => t('ID of the Buzz message.'),
    			'field' => array(
    				'handler' => 'views_handler_field_numeric',
    				'click sortable' => TRUE,
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_numeric',
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    		),
    		'msg_type_id' => array(
    			'title' => t('Message type ID in messages table'),
    			'help' => t('The ID of the message type.'),
    			'field' => array(
    				'handler' => 'views_handler_field',
    				'click sortable' => TRUE,
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_string',
    			),
    			'argument' => array(
    				'handler' => 'views_handler_argument_string',
    			),
    		),
    		'args' => array(
    			'title' => t('Message arguments'),
    			'help' => t('Arguments used to build the message'),
    			'field' => array(
    				'handler' => 'views_handler_field',
    				'click sortable' => TRUE,
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_string',
    			),
    			'argument' => array(
    				'handler' => 'views_handler_argument_string',
    			),
    		),
    		'created' => array(
    			'title' => t('Message creation time'),
    			'help' => t('The time in which the message was created.'),
    			'field' => array(
    				'handler' => 'views_handler_field_date',
    				'click sortable' => TRUE,
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort_date',
    			),
    			'filter' => array(
    			 	'handler' => 'views_handler_filter_date',
    			),
    		),
                   'usr_id' => array(
    			'title' => t('User ID'),
    			'help' => t('ID of the user that has generated this message'),
    			'relationship' => array(
    				'base' => 'users',
    				'field' => 'uid',
    				'handler' => 'views_handler_relationship',
    				'label' => t('Users'),
    			),
    			'field' => array(
    				'handler' => 'views_handler_field_numeric',
    				'click sortable' => TRUE,
    			),
    			'filter' => array(
    				'handler' => 'views_handler_filter_numeric',
    			),
    			'sort' => array(
    				'handler' => 'views_handler_sort',
    			),
    		),
    	);
    	
    	return $data;
    }
    

Lets look at what everything does.

First thing is defining an array. This array, called `$data`, will contain the
information describing to views how the data of our module is built. Each
table in out database will be represented by a separate entry in the the array
with the key being the database table name. In our case the module has two
tables, buzz_message_type and buzz_messages, and therefore the array has two
entries.

Each database table entry is in itself an array. In this array we give views
general information about the table as well information about each column.
Before we continue lets me explain what a base table in views is.

When creating a new view, you get to choose what will be used as a base table
for that view. That is, views will start with that table as its beginning
values and will expand from there as needed (through the use of
relationships). Those tables (such as node, users) are defined for views as
base tables. If you are interested in building views that are based upon your
modules information, it can be helpful to define one of your modules table as
a base table. Note that you can integrate your information with views without
defining a base table (we will see that soon). In our case, since we are
interested in creating views that represent only messages we will define the
messages table as a base table.

