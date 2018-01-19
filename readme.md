# log analysis project
this program analyses log data from a database using queries, which return the three most popular articles of all time, the three most popular authors of all time, and the days in which more than one percent of requests leads to an error.

## installation
* use a terminal
* (this program was written in python 2.7)
* download [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* download [vagrant](https://www.vagrantup.com/)
* download the [data](https://github.com/udacity/fullstack-nanodegree-vm) and [files](https://github.com/udacity/fullstack-nanodegree-vm) needed
* after downloading both, in your terminal `cd` into the downloaded 'files' and `cd` into vagrant file from your downloads
* run `vagrant up` in your terminal to start up your vagrant
* to load the data, after you cd into the vagrant directory, use the command `psql -d news -f newsdata.sql`
* to test the data, run `\dt` to see how many tables there arguments
* run `\dt table` (where 'table' is name of table) to see the schema of each table e.g `\dt log` to see log table, or `\dt authors` to see authors table, and `\dt articles` to see articles table.

### cloning the code
* to copy the project on your computer, open your terminal and do this: [git clone](https://github.com/afope/logproject.git) e.g $ `git clone <remote repo> <repo name>`
* you will find the **remote repo** link above by clicking on the green *"clone or download"* option in tab above the repository
* then run `cd <repo name>` in your terminal (*<repo name>* is whatever name you gave your repository in the terminal)
* this should open up the folder you just cloned from github
* open up your code editor


## usage
### running the code
* to run the code run the following command in your terminal: `python news.py > text.txt;`

### the following views were created:
#### the first query (most popular articles):
No views were created for the first query.

#### the second query (most popular authors):
first view : `create view article_views as select title, count(*) as views from articles a, log l where a.slug = substring(l.path,10) group by title order by views;`
second view : `create view article_author as select articles.title, authors.name from authors, articles where articles.author = authors.id group by name, title;`

#### the second query (highest error percentage):
first view : `create view title_views_author as select * from article_views natural join article_author;`
second view : `create view error_view as select name, sum(views) from title_views_author group by name order by sum desc limit 3;`


## contribution
it's a good example to learn working relational databases using psql and python.

## licensing
this code follows the [mit license](https://github.com/angular/angular.js/blob/master/LICENSE)
