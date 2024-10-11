#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;

gp_hash_table<K, V> hash_table;
cc_hash_table<K, V> hash_table;

tree<K, V/null_type, less<K>, rb_tree_tag, 
     tree_order_statistics_node_update> t;
t.find_by_order(k);
t.order_of_key(val);