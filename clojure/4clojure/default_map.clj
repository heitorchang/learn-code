(defn default-map [df ks]
  (loop [m {} k ks]
    (if (= (count k) 0)
      m
      (recur (conj m [(first k) df]) (rest k)))))
    
(default-map 0 [:a :b])
