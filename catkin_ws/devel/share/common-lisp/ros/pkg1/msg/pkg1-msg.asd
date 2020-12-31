
(cl:in-package :asdf)

(defsystem "pkg1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "two_ints" :depends-on ("_package_two_ints"))
    (:file "_package_two_ints" :depends-on ("_package"))
  ))