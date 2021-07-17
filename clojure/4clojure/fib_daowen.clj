(defn fib [n]
  (take n
        ((fn fib [x y]
           (lazy-seq
            (cons x (fib y (+ x y))))) 1 1)))
