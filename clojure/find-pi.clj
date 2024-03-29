(defn compare-float-sigfigs [s f]
  (if (or (>= f 3.1416) (<= f 3.14158))
    nil
    (let [float-string (str f)]
      (= s (subs float-string 0 (min (count float-string) (count s)))))))

(defn pi-sequence-term-ratio [idx]
  (let [fraction (/ 4 (+ 1 (* 2 idx)))]
    (if (even? idx) fraction (- fraction))))

(defn pi-sequence-term [idx]
  (double (pi-sequence-term-ratio idx)))

(defn find-pi []
  (let [pi-sequence (iterate (fn [[idx pi-approx]]
                               [(inc idx) (+ pi-approx (pi-sequence-term (inc idx)))])
                             [0 4])
        [final-idx final-estimate] (first (drop-while #(not (compare-float-sigfigs "3.14159" (second %))) pi-sequence))]
    [final-idx (pi-sequence-term-ratio final-idx) final-estimate]))
                   
;; [136120 4/272241 3.141599999994786]
;; after 136121 iterations (it started at 0)
