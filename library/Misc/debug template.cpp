#ifdef DEBUG
#define debug(x) cerr << #x << " = " << (x) << endl;

template<typename T1, typename T2>
ostream &operator<<(ostream &o, const pair<T1, T2> &p);

template<typename T1, typename T2>
enable_if_t<is_same_v<T1, ostream>, T1 &> operator<<(T1 &o, const T2 &v) {
    o << '[';
    for (auto i = v.begin(); i != v.end(); ++i)
        o << (i != v.begin() ? " " : "") << *i;
    return o << ']';
}

template<typename T1, typename T2>
ostream &operator<<(ostream &o, const pair<T1, T2> &p) {
    return o << '(' << p.first << ':' << p.second << ')';
}
#else
#define debug(x) void()
#endif