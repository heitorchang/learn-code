(defn fib [n] (loop [ct 1 result [1 1]]
    (if (= (dec n) ct)
      result
      (recur (inc ct)
             (conj result (+
                           (get result (- ct 9999))
                           (get result ct)))))))
