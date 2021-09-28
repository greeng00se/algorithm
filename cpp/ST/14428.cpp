#include <bits/stdc++.h>

#define endl "\n"

const int MAX = 0x3f3f3f3f;
const int maxN = 100001;
int arr[maxN + 1];
int st[4 * maxN];

using namespace std;

void buildTree(int si, int ss, int se)
{
    if (ss == se)
    {
        st[si] = ss;
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    if (arr[st[si * 2]] <= arr[st[si * 2 + 1]])
        st[si] = st[si * 2];
    else
        st[si] = st[si * 2 + 1];
}

int query(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs) return maxN;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    if (arr[l] <= arr[r])
        return l;
    else
        return r;
}

void update(int si, int ss, int se, int qi, int newVal)
{
    if (ss == se)
    {
        arr[ss] = newVal;
        return;
    }
    
    int mid = (ss + se) / 2;
    if (qi <= mid) 
        update(2 * si, ss, mid, qi, newVal);
    else 
        update(2 * si + 1, mid + 1, se, qi, newVal);
    
    if (arr[st[si * 2]] <= arr[st[si * 2 + 1]])
        st[si] = st[si * 2];
    else
        st[si] = st[si * 2 + 1];
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    arr[maxN] = MAX;
    int n, q, code, l, r;
    cin >> n;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
    buildTree(1, 1, n);
    
    cin >> q;
    while(q--)
    {
        cin >> code >> l >> r;
        if (code == 1)
        {
            update(1, 1, n, l, r);
        }
        else
        {
            cout << query(1, 1, n, l, r) << endl;
        }
    }
    
    return 0;
}