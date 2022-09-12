#|

sbcl --disable-debugger

(progn
  (load "/home/heitor/experimental/lisp/cmd-adder.lisp")
  (sb-ext:save-lisp-and-die "/home/heitor/bin/add" :toplevel #'main :executable t))

|#

(defun add-strings (strs)
  (apply #'+ (mapcar #'parse-integer strs)))

(defun main ()
  (prin1 (add-strings (uiop:command-line-arguments)))
  (terpri))

;; multiply
;; https://stackoverflow.com/questions/1495475/parsing-numbers-from-strings-in-lisp
(defun parse-string-to-floats (line)
  (loop
    :with n := (length line)
    :for pos := 0 :then chars
    :while (< pos n)
    :for (float chars) := (multiple-value-list
            (read-from-string line nil nil :start pos))
    :collect float))

(defun mul-a-b (strs)
  (apply #'* (parse-string-to-floats strs)))

(defun calc (str-list)
  (prin1 (mul-a-b (format nil "~{~A ~}" str-list)))
  (terpri))

(defun main ()
  (calc (uiop:command-line-arguments)))


(defun div-a-b (strs)
  (/ (apply #'/ (parse-string-to-floats strs)) 1.0))

(defun calc (str-list)
  (prin1 (div-a-b (format nil "~{~A ~}" str-list)))
  (terpri))

(defun main ()
  (calc (uiop:command-line-arguments)))
