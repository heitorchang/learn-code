(defn rotate2 [deque]
  (if (<= (.size deque) 2)
    deque
    (let [fst (.remove deque)
          snd (.remove deque)]
      (.addLast deque fst)
      (.addLast deque snd)
      deque)))

(defn iter [d a]
  (if (= (.size d) 0)
    a
    (let [newlst (rotate2 d)
          st (.removeLast d)]
      (iter newlst (conj a st)))))

(defn pjCircle [s w]
  (let [deque (java.util.ArrayDeque. (range 1 (+ 1 s)))
        a (vector)]
    (drop (- s w) (iter deque a))))

(pjCircle 6 4)


