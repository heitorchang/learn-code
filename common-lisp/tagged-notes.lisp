(defparameter *tagged-notes-lisp-files* "/home/heitor/tmp/taggednoteslisp/")

(defun split-by-space (str)
  (loop for i = 0 then (1+ j)
        as j = (position #\space str :start i)
        collect (subseq str i j)
        while j))

(defun write-file (filename contents)
  (with-open-file (out (concatenate 'string *tagged-notes-lisp-files* filename ".lisp")
                       :direction :output
                       :if-exists :supersede)
    (print contents out)))

(defun add-post (title body tags)
  "Save (title body) to a file whose name is the universal-time, and save
this universal-time into files whose names are the tags (space-separated)"
  
  (let ((timestamp-str (write-to-string (get-universal-time)))
        (tag-list (split-by-space tags)))
    (write-file timestamp-str (list title body))
    (dolist (a-tag tag-list)
      (write-file a-tag (list timestamp-str)))))
