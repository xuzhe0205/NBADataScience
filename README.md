# A web crawler scraping NBA data & Bayesian Model for NBA game analysis
------------------------------------

### Description: This portion in the project serves as a crawler that help scraping and retrieving helpful data from the nba.com website to assist Bayesian modeling and data analysis in the Jupyter notebook

* Files: 
        ./webcrawler
            nbacrawler.py
            ./data
                nbastats.csv  
        Hoston_Rockets_Analysis.ipynb
        NBATeamsAnalysis.ipynb   
        

### Instructions:

    1. If you have not installed python, go to `https://www.python.org/downloads/` to download python, and install python3 by going to terminal and type: ```brew install python3```

    2. Install required libraries for this project:
        numpy: ```pip3 install numpy```
        request: ```pip3 install request```
        pandas: ```pip3 install pandas```
        bs4: ```pip3 install bs4```
        selenium: ```pip3 install selenium```

    3. Run the code ```nbacrawler.py```

    4. Run ```NBATeamsAnalysis.ipynb``` and ```Hoston_Rockets_Analysis.ipynb``` to use the Bayesian model to drive prediction and data analysis

        * ```Hoston_Rockets_Analysis.ipynb``` contains the Bayesian model that firstly load the traditional and advanced NBA team stats, then construct linear regressions that interpret the relation between `DREB`, `FG%` and various attributes from the data, and the `WIN%` of NBA team. Lastly, the `team_model` Bayesian model is built to drive `WIN% `prediction for NBA teams

        * ```NBATeamsAnalysis.ipynb```: similar to previous notebook, this notebook contians Bayesian model for analysis and prediction of `WIN%` for one NBA team: Houston rockets. It reads Houston Rockets stats for the past 23 seasons, and build the Bayesian model that takes `AST`, `REB` etc. as attributes, drive prediction and draw conclusion

        * Click "Launch under the "Jupyter Notebook" in the Anaconda Navigation

        * Or, start a terminal window, ```cd``` to your local folder where this Jupyter Notebook locates, and type ```jupyter notebook``` to start the Jupyter Notebook
        
        * Go to the first code in the Notebook, and press "Shift + Enter" to check the result or output for each line of code


### Notes:

    Multiples data are scraped and located in the `data` folder, in which, only `HoustonRocket`, `teamstats2019` and `teamadvancedstats2019` are used

### Acknowledgement
    https://nycdatascience.com/blog/student-works/web-scraping/web-scraping-nba-stats/
    Stackoverflow
    python.org
    
