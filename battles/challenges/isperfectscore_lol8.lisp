(defclass test-paper1 ()
  (ans1))

(defclass test-paper2 (test-paper1)
  (ans2))

(defclass test-paper3 (test-paper2)
  (ans3))

(if (not (boundp '*ran-init*))
    (progn
      (defgeneric get-ans1 (test-paper))
      (defgeneric get-ans2 (test-paper))
      (defgeneric get-ans3 (test-paper))

      (defmethod get-ans1 ((test-paper test-paper1)) 
        (slot-value test-paper 'ans1))

      (defmethod get-ans1 ((test-paper test-paper2))
        (slot-value test-paper 'ans1))

      (defmethod get-ans1 ((test-paper test-paper3))
        (slot-value test-paper 'ans1))

      (defmethod get-ans2 ((test-paper test-paper2))
        (slot-value test-paper 'ans2))

      (defmethod get-ans2 ((test-paper test-paper3))
        (slot-value test-paper 'ans2))

      (defmethod get-ans3 ((test-paper test-paper3))
        (slot-value test-paper 'ans3))))

(defparameter *ran-init* t)

(defun isPerfectScore (ans1 ans2 ans3)
  (defparameter *test-paper1* (make-instance 'test-paper1))
  (defparameter *test-paper2* (make-instance 'test-paper2))
  (defparameter *test-paper3* (make-instance 'test-paper3))

  (setf (slot-value *test-paper1* 'ans1) ans1)
  
  (setf (slot-value *test-paper2* 'ans1) (slot-value *test-paper1* 'ans1))
  (setf (slot-value *test-paper2* 'ans2) ans2)
  
  (setf (slot-value *test-paper3* 'ans1) (slot-value *test-paper2* 'ans1))
  (setf (slot-value *test-paper3* 'ans2) (slot-value *test-paper2* 'ans2))
  (setf (slot-value *test-paper3* 'ans3) ans3)
  
  (cond ((equalp (get-ans1 *test-paper3*) t)
         (cond ((equalp (get-ans2 *test-paper3*) t)
                (cond ((equalp (get-ans3 *test-paper3*) t) t)
                      ((equalp (get-ans3 *test-paper3*) nil) nil)))
               ((equalp (get-ans2 *test-paper3*) nil)
                (cond ((equalp (get-ans3 *test-paper3*) t) nil)
                      ((equalp (get-ans3 *test-paper3*) nil) nil)))))
        ((equalp (get-ans1 *test-paper3*) nil)
         (cond ((equalp (get-ans2 *test-paper3*) nil)
                (cond ((equalp (get-ans3 *test-paper3*) t) nil)
                      ((equalp (get-ans3 *test-paper3*) nil) nil)))
               ((equalp (get-ans2 *test-paper3*) nil)
                (cond ((equalp (get-ans3 *test-paper3*) t) nil)
                      ((equalp (get-ans3 *test-paper3*) nil) nil)))))))
