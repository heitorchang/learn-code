;; times out

(defun rotleft2 (lst)
  (if (= (length lst) 1)
      lst
    (concatenate 'list (cddr lst) (list (car lst) (cadr lst)))))

(defun iter (surv rm)
  (if (null rm)
      surv
    (let ((newlst (rotleft2 rm)))
      (iter (cons (car (last newlst)) surv) (butlast newlst)))))

(defun revwinners (s w)
  (let ((a (soRange 1 s))
        (surv '()))
    (iter surv a)))

(defun pjCircle (s w)
  (let ((winners (reverse (revwinners s w))))
    (subseq winners (- s w) s)))

(defun soRange (min max &optional (step 1))
  ;; stack overflow
  (when (<= min max)
    (cons min (soRange (+ min step) max step))))
