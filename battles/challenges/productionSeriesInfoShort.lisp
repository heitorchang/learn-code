(defun productionSeriesInfo (g r s v)
  (labels ((q (n) (write-to-string n))
           (d (a b c) (concatenate 'string a b c))
           (f (w z)  ; compute total ingredients for one series
              (if (null w)
                  z  ; total
                (f (cdr w)
                   (let ((m (car w)))
                     (cond ((= m 1) (+ r z))  ; recipe 1
                           ((= m 2) (+ s z))  ; recipe 2
                           (t (+ m z))))))))  ; series value
          (let* ((p (coerce v 'list))  ; CodeSignal lists are vectors
                 (c (f p 0))  ; ingredients consumed in one series
                 (p (floor g c)))  ; number of full series
            (cond ((= 0 p) (list "Out of ingredients!"
                                          (d "Missing "
                                             (q (- c g)) 
                                             " ingredients")))
                  ((= 1 p) (list "Ok"))
                  (t (list "Ok" (d "Ingredients for " 
                                   (q (- p 1)) 
                                   " more series")))))))
