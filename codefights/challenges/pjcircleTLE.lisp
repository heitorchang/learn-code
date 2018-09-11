(defun range (lim i sofar)
  (if (= i lim)
      sofar
    (if (= i 0)
        '()
      (range lim (+ 1 i) (cons (- lim i) sofar)))))

(defun unnest (x)
  ;; stack overflow
  (labels ((rec (x acc)
    (cond ((null x) acc)
      ((atom x) (cons x acc))
      (t (rec (car x) (rec (cdr x) acc))))))
          (rec x nil)))

(defun rotleft2 (lst)
  (unnest (cons (cddr lst) (list (car lst) (cadr lst)))))

(defun iter (surv rm)
  (if (null rm)
      surv
    (let ((newlst (rotleft2 rm)))
      (iter (cons (car (last newlst)) surv) (butlast newlst)))))

(defun revwinners (s w)
  (let ((a (range (+ 1 s) 1 '()))
        (surv '()))
    (iter surv a)))

(defun pjCircle (s w)
  (let ((winners (reverse (revwinners s w))))
    (subseq winners (- s w) s)))
