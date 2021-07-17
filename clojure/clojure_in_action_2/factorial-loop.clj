(defn fact-loop [n]
  (loop [current n fact 1]
    (if (= current 1)
      fact
      (recur (dec current) (* fact current)))))


(doseq [x [:a :b :c]]
  (println x))
