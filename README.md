1) clone the repository / download
2) if you don't have python/django installed, proceed to django documentation
3) in a terminal, get inside the first snp_site directory and run the server via ```py manage.py runserver``` on windows or ```python manage.py runserver``` on linux.
4) site should be available at [127.0.0.1:8000/](http://127.0.0.1:8000/)

notes:
1) This is an app without real data, but with some artificial mockup data added for demonstration. 
2) Functionality: choose a species from the cards in the top panel below navigation, and then search for specified SNPs (single nucleotide polymorphisms) in collected samples for that species.
3) A download button is also available, it allows the user to download the data returned from a search query as .csv.
4) the "show in browser" button is not doing anything, but in a real implementation it could show the context of the SNP in a reference sequence
5) the "region" field lets the user specify the name/number of the chromosome in which we are looking for SNPs.
6) the MAF min. value and max value lets the user specify a range of MAF values that the paginated table below will show SNPs for. maximal MAF is 0.49 in this case
7) For admin functionality checks, default superuser used during development:
   user: bs419396
   password: 1234
   
