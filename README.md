# backslash-trash
**Backslash Trash plots locations of trash cans in Boston compared to population density, showing where to build more.**
Winner of the Two Sigma Category Award at SheHacks Boston: Best Use of Open Source Data for Social Good!

Built with: **Python, HTML, Javascript, GeoJSON, GoogleMaps Javascript API**

![A screenshot of the \Trash app!](https://github.com/elizabethcarney/backslash-trash/blob/master/%5CTrash%20Screenshot.png)

**INSPIRATION:** We wanted to learn about databases while simultaneously helping our community.

**WHAT IT DOES:** By comparing the locations of existing trash cans to population density across Boston, Backslash Trash makes it easy to visualize places where new trash cans are most needed. 

**HOW WE BUILT IT:** We started with a dataset from Analyze Boston that included the coordinates of each Big Belly trash can in Boston. We then extracted the latitudinal and longitudinal pairs from the data into a JavaScript file using string manipulation and file handling in Python. Next, we utilized the GoogleMaps JavaScript API in order to place a marker at the location of each trash can. We overlaid a heat map detailing population density in the Boston area and used HTML to separate the data from the rest of the set. We then created a color code in HTML to visualize which areas are most densely populated. 

**CHALLENGES WE RAN INTO:** Aside from Python, all of the APIs and programming languages we used were completely new to us. Extracting data from large sets was definitely challenging, as was familiarizing ourselves with the GoogleMaps API. However, our biggest struggle was deducing how to overlay and color-code the population density heat map. We sought help from the SheHacks mentors to set feasible goals to keep us on track towards realizing our final product.

**ACCOMPLISHMENTS WE'RE PROUD OF:** We are extremely proud of the finished product as a whole, especially when we think about how much we have learned just in the course of the weekend. More specifically, seeing our data visuals appear on the GoogleMap for the first time was so rewarding. These breakthroughs gave us the confidence to keep coding, even though we often were working with applications that were completely new to us. 

**WHAT WE LEARNED:** We learned so much! We are so grateful to all of the mentors who generously volunteered their time in order help us realize our dream, \Trash. We now feel comfortable coding in HTML and JavaScript, working with large datasets, and using the GoogleMaps API, all new skills for us. Most importantly, we learned that we can do anything we set our minds to, through the powers of collaboration and hard work! 

**WHAT'S NEXT:** We have many ideas for how to move forward with \Trash. One of the great things about our project is that it is scalable and could easily be implemented in other cities around the world. Given more time, we would host our application on a server so that it can be accessed remotely. Additionally, we would like to continue to add overlays to the app such as urban development, economic growth, and traffic statistics in order to consider more factors when choosing where to place new trash cans. We are happy with what we have produced, but we acknowledge that there's much more we **CAN** do with \Trash.
