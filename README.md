This is a Chinese hospital query information program.
When you run command like this:
python queryHospital.py provinceName

The program will show us third-grade class-A hospital in one province.
And it's a demo project for using tornado Async programming.

The program's archicture is like scrapy(I think).  There are 4 parts in the program: Runner, Spider, Filter and Pipeline
What Runner do is load spider with filter and pipeline
When spider fetch page, it will go through filter and pipelines.
Filter is mainly concern about if parsed item by spider match our request, and Pipeline will do something to item, like
save item to database, or print item information.

They are showed as this diagram:
   ----------	    ----------
   | Runner | ----> | Spider | <-------------------- | Web
   ---------- fire  ----------   fetch information
   		    	|
			| parsed item
			|
		       \ /
   		    -----------
		    | Filters |
		    -----------
		        |
			| filter matched item
			|
		       \ /
		    -------------
		    | Pipelines |
		    -------------
	       Pipeline is the end of item flow
	       It will do something to item.