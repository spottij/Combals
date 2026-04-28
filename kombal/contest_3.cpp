#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    int weight;
};

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");

    int n;
    if (!(in >> n)) return 0;
    vector<vector<Edge>> adj(n + 1);

    for (int v = 1; v <= n; ++v) {
        int u;
        while (in >> u && u != 0) {
            int w;
            in >> w;
            adj[u].push_back({v, w});
        }
    }

    int start, target;
    in >> start >> target;

    // Дейкстра
    vector<long long> dist(n + 1, INF);
    vector<int> parent(n + 1, 0);
    dist[start] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        long long d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (d > dist[u]) continue;

        for (auto& edge : adj[u]) {
            if (dist[u] + edge.weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + edge.weight;
                parent[edge.to] = u;
                pq.push({dist[edge.to], edge.to});
            }
        }
    }

    if (dist[target] == INF) {
        out << "N";
    } else {
        out << "Y" << endl;
        vector<int> path;
        for (int v = target; v != 0; v = parent[v]) {
            path.push_back(v);
        }
        reverse(path.begin(), path.end());

        for (int i = 0; i < path.size(); ++i) {
            out << path[i] << (i == path.size() - 1 ? "" : " ");
        }
        out << endl << dist[target];
    }

    return 0;
}