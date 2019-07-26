<p align="center">
  <a href="https://github.com/s0md3v/Orbit"><img src="https://i.ibb.co/bXsZHW0/orbit.png" alt="Orbit"></a>
  <br>
  <b>ＯＲＢＩＴ</b>
</p>
<h4 align="center">Blockchain Transactions Investigation Tool</h4>
<p align="center">
  <a href="https://github.com/s0md3v/Orbit/releases">
    <img src="https://img.shields.io/github/release/s0md3v/Orbit.svg">
  </a>
  <a href="https://github.com/s0md3v/Orbit/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/Orbit.svg">
  <img src="https://img.shields.io/badge/python-> 3.2-blue.svg">
  </a>
</p>

![graph-demo](https://i.ibb.co/rx76Ryt/Screenshot-2019-07-26-03-41-34.png)

### Introduction
Orbit is designed to explore network of a blockchain wallet by recursively crawling through transaction history. The data is rendered as a graph to reveal major sources, sinks and suspicious connections.

> **Note:** Orbit only runs on Python 3.2 and above.

### Usage

Let's start by crawling transaction history of a wallet
```
python3 orbit.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F
```
Crawling multiple wallets is no different.
```
python3 orbit.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F,1ETBbsHPvbydW7hGWXXKXZ3pxVh3VFoMaX
```
Orbit fetches last 50 transactions from each wallet by default, but it can be tuned with `-l` option.
```
python3 orbit.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -l 100
```
Orbit's default crawling depth is 3 i.e. it fetches the history of target wallet(s), crawls the newly found wallets and then crawls the wallets in the result again. The crawling depth can be increased or decresead with `-d` option.
```
python3 orbit.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -d 2
```
Wallets that have made just a couple of interactions with our target may not be important, Orbit can be told to crawl top N wallets at each level by using the `-t` option.
```
python3 orbit.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -t 20
```
If you want to view the collected data with a graph viewer of your choice, you can use -o option.
```
python3 orbit.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -o output.graphml
```
Support Formats

- `graphml` (Supported by most graph viewers)
- `json` (For raw processing)


This is your terminal dashboard.

![demo-terminal](https://i.ibb.co/pZG24vT/Screenshot-2019-07-26-08-07-10.png)


### Visualization
Once the scan is complete, the graph will automatically open in your default browser. If it doesn't open, open `quark.html` manually.
Don't worry if your graph looks messy like the one below or worse.

![graph-setup](https://i.ibb.co/xJ38DF9/Screenshot-2019-07-26-08-21-18.png)

Select the **Make Clusters** option to form clusters using community detection algorithm. After that, you can use **Color Clusters** to give different colors to each community and then use **Spacify** option to fix overlapping nodes & edges.

![graph-fixed](https://i.ibb.co/SsGhkJN/Screenshot-2019-07-26-09-21-08.png)

The thickness of edges depends on the frequency of transactions between two wallets while the size of a node depends on both transaction frequency and the number of connections of the node.

As Orbit uses ![Quark](https://github.com/s0md3v/Quark) to render the graph, more information about the various features and controls is available in Quark's README.
