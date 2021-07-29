;; check if stack blows up

(defun simple-recursion (counter)
  (format t "~a~%" counter)
  (if (= counter 1e6)
      'reached-million
      (simple-recursion (1+ counter))))
