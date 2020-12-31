; Auto-generated. Do not edit!


(cl:in-package pkg1-msg)


;//! \htmlinclude two_ints.msg.html

(cl:defclass <two_ints> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:fixnum
    :initform 0)
   (b
    :reader b
    :initarg :b
    :type cl:fixnum
    :initform 0))
)

(cl:defclass two_ints (<two_ints>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <two_ints>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'two_ints)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg1-msg:<two_ints> is deprecated: use pkg1-msg:two_ints instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <two_ints>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg1-msg:a-val is deprecated.  Use pkg1-msg:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <two_ints>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg1-msg:b-val is deprecated.  Use pkg1-msg:b instead.")
  (b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <two_ints>) ostream)
  "Serializes a message object of type '<two_ints>"
  (cl:let* ((signed (cl:slot-value msg 'a)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'b)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <two_ints>) istream)
  "Deserializes a message object of type '<two_ints>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'b) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<two_ints>)))
  "Returns string type for a message object of type '<two_ints>"
  "pkg1/two_ints")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'two_ints)))
  "Returns string type for a message object of type 'two_ints"
  "pkg1/two_ints")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<two_ints>)))
  "Returns md5sum for a message object of type '<two_ints>"
  "e01e889cb1a7965611513515df5899bf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'two_ints)))
  "Returns md5sum for a message object of type 'two_ints"
  "e01e889cb1a7965611513515df5899bf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<two_ints>)))
  "Returns full string definition for message of type '<two_ints>"
  (cl:format cl:nil "int16 a~%int16 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'two_ints)))
  "Returns full string definition for message of type 'two_ints"
  (cl:format cl:nil "int16 a~%int16 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <two_ints>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <two_ints>))
  "Converts a ROS message object to a list"
  (cl:list 'two_ints
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
))
