(defparameter *h* (make-hash-table))
(setf (gethash 'a *h*) 1)
(setf (gethash 'b *h*) 2)

(defun add-1 (sym) 
  (+ 1 (gethash sym *h*)))

(defun add-many (syms)
  (reduce #'+ (mapcar (lambda (s) (gethash s *h*)) syms)))

;; try (add-many '(a b c))
