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
* to run the code run the following command in your terminal: `python news.py;`

### the following views were created:
#### the first query (most popular articles):
No views were created for the first query.

#### the second query (most popular authors):
first view : `CREATE OR REPLACE VIEW article_views as SELECT title, count(*) as views FROM articles a, log l WHERE a.slug = substring(l.path,10) GROUP BY title ORDER BY views;`
second view : `CREATE OR REPLACE VIEW article_author as SELECT articles.title, authors.name FROM authors, articles WHERE articles.author = authors.id GROUP BY name, title;`

#### the third query (highest error percentage):
`CREATE OR REPLACE VIEW error_view as SELECT date(time) as date, round(100.0*sum(case log.status when '200 OK'
then 0 else 1 end)/count(log.status),2) as percentage_error FROM log GROUP BY date                              
ORDER BY percentage_error desc;`


## contribution
it's a good example to learn working on relational databases using psql and python.

## licensing
this code follows the [mit license](https://github.com/angular/angular.js/blob/master/LICENSE)
