;; Auto-generated. Do not edit!


(when (boundp 'pkg1::two_ints)
  (if (not (find-package "PKG1"))
    (make-package "PKG1"))
  (shadow 'two_ints (find-package "PKG1")))
(unless (find-package "PKG1::TWO_INTS")
  (make-package "PKG1::TWO_INTS"))

(in-package "ROS")
;;//! \htmlinclude two_ints.msg.html


(defclass pkg1::two_ints
  :super ros::object
  :slots (_a _b ))

(defmethod pkg1::two_ints
  (:init
   (&key
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; int16 _a
    2
    ;; int16 _b
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _a
       (write-word _a s)
     ;; int16 _b
       (write-word _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _a
     (setq _a (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _b
     (setq _b (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get pkg1::two_ints :md5sum-) "e01e889cb1a7965611513515df5899bf")
(setf (get pkg1::two_ints :datatype-) "pkg1/two_ints")
(setf (get pkg1::two_ints :definition-)
      "int16 a
int16 b

")



(provide :pkg1/two_ints "e01e889cb1a7965611513515df5899bf")


