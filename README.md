# Orbit

Give it a blockchain based crypto wallet address and it will crawl 3 levels deep in transaction data to plot a graph out of the information.

![orbit demo](https://image.ibb.co/kMoLz8/Screenshot_2018_07_10_21_13_30.png)

![quark demo](https://image.ibb.co/efGR6o/Screenshot_2018_07_10_21_23_13.png)

## Usage
Run orbit.py with python3 as follows

`python3 orbit.py`

Enter the wallet address

```
  __         
 |  |  _ |  ' _|_
 |__| |  |) |  |  
 
Enter a wallet address: xxxxxxxxxxxxxxx
```
Now orbit will scrape wallets through blockchain API and once its done, a json file will be generated.\
Next thing is to plot a graph for which we will be using [quark framework](https://github.com/s0md3v/Quark) which is also written by me :D

Clone Quark and navigate to the Quark directory and feed the json file to quark.py as follows:

`python quark.py /path/to/file.json`

And that's it! Your job is done here, open `quark.html` to see your graph ^_^

## Warning!
The size of nodes (dots) and edges (lines) depends on the transactions made by that address to other members of the scope.\
So the size of nodes can be ridiculosly big but don't get scared, just click on `stabilize` option in the sidebar and leave the rest to quark.\
Also, if the node lables are getting on the way, click on the `Node Lables` option to turn that off.\
The last thing is that there are going to be a lot of nodes that aren't interesting like a wallet that has made only one transaction.
Such nodes will just make your graph ugly. To fix this, click on the `clean` option which will delete such insignificant nodes.
More information about how to interact with the graph can be found on [Quark's readme](https://github.com/s0md3v/Quark).
