;;; solve towers of hanoi
;;; idea: recursive solution

(defun unused-peg (source destination)
  (let ((pegs '(A B C)))
    (first (set-difference pegs (list source destination)))))

(defun move (size source destination)
  "Move a tower of size disks from source to destination. Pegs are named A, B, and C"
  (let ((unused-peg (unused-peg source destination)))
    (when (> size 0)
      (move (- size 1) source unused-peg)
      (print `(move ,size from ,source to ,destination))
      (move (- size 1) unused-peg destination))))
      
