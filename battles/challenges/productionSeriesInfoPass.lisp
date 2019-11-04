;;;; Notes:
;; (calctot initially built a whole new list and reversed it.
;; hidden tests failed because of this but there weren't any notices
;; keeping total in a single integer passed


(defun productionSeriesInfo (ingredients recipe1 recipe2 productionSeriesVec)
  (labels ((calctot (productionSeries tot)
                    (if (null productionSeries)
                        tot
                        (calctot (cdr productionSeries) 
                                 (cond ((= (car productionSeries) 1) (+ recipe1 tot))
                                     ((= (car productionSeries) 2) (+ recipe2 tot))
                                     (t (+ (car productionSeries) tot)))))))
          (let* ((productionSeries (coerce productionSeriesVec 'list))
                 (constot (calctot productionSeries 0))
                 (canproduce (floor ingredients constot)))
            (cond ((= 0 canproduce) (list "Out of ingredients!"
                                          (concatenate 'string 
                                                       "Missing "
                                                       (write-to-string (- constot ingredients)) 
                                                       " ingredients")))
                  ((= 1 canproduce) (list "Ok"))
                  (t (list "Ok" (concatenate 'string 
                                             "Ingredients for " 
                                             (write-to-string (- canproduce 1)) 
                                             " more series")))))))
