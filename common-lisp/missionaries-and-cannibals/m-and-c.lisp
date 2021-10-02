(defun valid-state (state)
  (and (<= 0 (first state) 1)
       (<= 0 (second state) 3)
       (<= 0 (third state) 3)
       (<= 0 (fourth state) 3)
       (<= 0 (fifth state) 3)
       (if (> (second state) 0)
           (>= (second state) (third state))
           t)
       (if (> (fourth state) 0)
           (>= (fourth state) (fifth state))
           t)
       (= 3 (+ (second state) (fourth state)))
       (= 3 (+ (third state) (fifth state)))))

(defun winning-state (state)
  (equal state '(0 0 0 3 3)))

(defun move-m-c (state m c)
  "Move m missionaries and c cannibals given a state"
  (let ((new-state (if (= (first state) 1)
                       (list 0 (- (second state) m) (- (third state) c) (+ (fourth state) m) (+ (fifth state) c))
                       (list 1 (+ (second state) m) (+ (third state) c) (- (fourth state) m) (- (fifth state) c)))))
    (if (valid-state new-state)
        new-state
        nil)))

(defun next-states (state)
  (remove-if #'null (list
                     (move-m-c state 0 1)
                     (move-m-c state 1 0)
                     (move-m-c state 0 2)
                     (move-m-c state 2 0)
                     (move-m-c state 1 1))))

(defun simulate (state paths-taken)
  (dolist (next-state (next-states state))
    (when (not (member next-state paths-taken :test #'equal))
      (if (winning-state next-state)
          (progn (print (reverse paths-taken)) (print next-state))
          (simulate next-state (cons next-state paths-taken))))))

;; eval (simulate '(1 3 3 0 0) '((1 3 3 0 0)))
;; ((1 3 3 0 0) (0 3 1 0 2) (1 3 2 0 1) (0 3 0 0 3) (1 3 1 0 2) (0 1 1 2 2) (1 2 2 1 1) (0 0 2 3 1) (1 0 3 3 0) (0 0 1 3 2) (1 0 2 3 1))
;; (0 0 0 3 3) 
