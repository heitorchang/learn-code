(defmacro parse-backquote (vars code)
  `(let (,@(read-from-string vars))
     ,(read-from-string code)))

;; (parse-backquote "((bob 51) (amy 23))" "`(,amy ,bob jack)")
;; => (23 51 JACK)
;; require capitalization
