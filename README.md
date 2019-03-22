# A web crawler scraping NBA data & Bayesian Model for NBA game analysis
------------------------------------

### Description: 

A data science project that using linear regression and Bayesian Model to analyze NBA game performance and drive predictions.  This project involves: firstly writing a web crawler in Python to scrape various data from NBA.com; secondly manipulating data to: perform linear regression analyzing the correlation and clustering among all related data; and building Bayesian Model with Markov chain Monte Carlo Sampling to drive team-win prediction for NBA teams in general, and one randomly chosen NBA team: Houston Rockets as well.


* Files: 
```
        ./webcrawler
            nbacrawler.py
            ./data
                nbastats.csv  
        ./assests
             images(.png)
        Hoston_Rockets_Analysis.ipynb
        NBATeamsAnalysis.ipynb   
```        

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
    

### Analysis

#### For All NBA Teams (up to 02/21/2019)

Start this portion of the project by doing data mining and inspection on the `teamstats2019.csv` and `teamadvancedstats2019.csv`. Following the current trend of NBA gameplay that analysts and NBA fans expect, 
there is a boxplot that can deliever a clear yet funny interpretation of todays NBA offense, especially 
relationship between three points attempts `3PA` and winning percentage `WIN%`:

![3paBoxplot](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/3pabox.png)

Moving on, I used `heatmap` from `seaborn` package to visualize the correlation among all attributes from 
both traditional and advanced NBA team data. And then slice them into smaller portions of heatmap accordingly, 
from which we can tell and select the meaningful and influencial attribute for later data science modeling:
(`EFG%`, `DREB`, `DEFRTG`, `OFFRTG`, `+/-` and `FG%`)

![hp1](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/hp1.png)


![hp2](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/hp2.png)

Applying linear regression on various selected attributes, we can observe the clutering and the least square 
relation among the data. For example, from the linear regression plot for defense rating vs. game win, we can 
preliminarily see that there is a negative relation between the two based on value, meaning that the lower 
points allow (account for better defense) help winning the game:

![lina](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/lina.png)


Going into the next step: building bayesian model to drive prediction!

After specifying the associated parameters for attributes and determining the specific types of distributions, we use the `NUTS`(the No U-Turn Sampler) method to obtain posterior estimates for later prediction. And as observed, the choice of distribution seems to be quite well, posteriors attributes gits. For examples, with sample data generated, those top NBA teams are still winning on the same trend as original data. 

![post1](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/post1.png)

![post2](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/post2.png)


Use sample_ppc from pymc3 to generate 6000 simulated data as testing set for the team_model to check if this model fits

Sampling from the posterior predictive distribution is straighforward in PyMC3. The sample_ppc function draws posterior predictive checks from all of the data likelihoods.

* By estimating these distribution plots, about 12 out of 15 posterior distributions are showing that the posterior estimates and the team_model genearally fit the prediction that this Bayesian model drives，and so they are in a good fit!

![post3](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/post3.png)


With this Bayesian model ready, further winning prediction for the NBA teams can proceed. 

First, the equation `win_samples = Normal.dist(inters + fgpers + drebs + pms + deftngs+offtngs + efgpers, sigs).random()`
was used to drive prediction for the NBA teams. With that, we can estimates the probability of NBA teams having a WIN% 
of over 50%, meaning that, based on the team_model, there are about 19.9% of the 30 NBA teams can end up with 50% WIN%:

![win1](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/win1.png)

Want to see how those attributes (`EFG%`, `DREB`, `DEFRTG`, `OFFRTG`, `+/-` and `FG%`) weigh in? manipulate them by:

* Decrease defense rating by 20% (because the better the defense the lower the rating, i.e. the points allowed for opponens)
* Increase effective field goal percentage and defense rebound by 20%, meaning that the teams execute more efficient offense, maintain better shot selections and grabbing more defensive rebound in the NBA game

![win2](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/win2.png)

With the same logic: if teams play much worse defense in the game (value of defense rating increased by 40%) and grabing less defensive rebound (also account for bad defense) and taking inefficient shots(lower effective field goal percentage by 20%), the winning rate (of teams having WIN% over 50%) decreased almost 0.4% to 19.58%

![win3](https://raw.githubusercontent.com/xuzhe0205/NBADataScience/master/assets/win3.png)

<br>

#### For a Randomly Selected NBA Team: Houston Rockets

* In this portion of the project. I used the similar approach and procedures to build the Bayesian Model that drive winning prediction for the Houston Rockets to see why they are shooting good amount of three pointers, and yet still not among the top NBA teams (up to now 02/21/2019).

* Another purpose of conducting this portion of the project is to confirm with the previous portion. And see if there is any anormalies and if the conclusions matched

### Conclusion

* To result in better team winning rate, attributes/execution of EFG%, DREB, DEFRTG, OFFRTG, +/- and FG% are the key for gameplay execution during the NBA game.

* More specifically, maintaining better and more efficient shot selection(higher EFG%), better defense (more defensive rebound DREB, less oppenents' point allowed DEFRTG), and/or better offense (Offense rating OFFRTG, points deficit +/- and better shot selection and efficiency FG%) can help the team win more game and increase the WIN%


### Future Improvement

1. After acquiring/scraping more data for NBA players for each NBA team specifically, I can also use Bayesian Model Analysis to determine which players can increase the team's chance of winning, or maybe acquiring which player from another team.

2. With respect to acquiring other players, what I would do is to build a bayesian model (linear) where the top (e.g. 5) players figure as parameters. Then I would first see which player has the highest associated coefficient. That is the most valuable player for the team. Then I would see how these players fare against other teams. Are there teams they play consistently well against, or consistently poor against (with personal statistics). Then I would also build a team model: Who do the specific NBA team play poor against? Now I have a model to make some decisions on. For example, how about drafting a player that plays well against teams that a specific NBA team play poor against? What if that player does not figure amongst the top players of the team he belongs to? Then that team might be ok with trading him to that NBA team.

<br>

### Acknowledgement
    Stackoverflow
    python.org
    
