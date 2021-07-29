(defun find-pi (current-estimate)
  (dotimes (index 500000)
    (let ((fraction (if (= 0 (mod index 2))
                        (/ 4.0d0 (+ 1 (* 2 index)))
                        (/ -4.0d0 (+ 1 (* 2 index))))))
      (setf current-estimate (+ current-estimate fraction))
      (format t "~a ~a ~,9a ~%" index fraction current-estimate)
      (if (string= "3.14159" (subseq (with-output-to-string (output)
                                       (format output "~,12f" current-estimate)) 0 7))
          (progn
            (format t "~a ~a" index current-estimate)
            (return))))))

(find-pi 0)
;; returns index 136120

