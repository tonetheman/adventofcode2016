#lang racket

(define env (make-hash))

(define (cpy arg1 arg2)
  (cond
    [(number? arg1) (hash-set! env (symbol->string arg2) arg1)]
    [(symbol? arg1) (hash-set! env (symbol->string arg2) (hash-ref env (symbol->string arg1)))]
  )
)

(define (inc arg1)
  (define tmp (hash-ref env (symbol->string arg1)))
  (define res (+ tmp 1))
  (hash-set! env (symbol->string arg1) res)
)

(define (dec arg1)
  (define tmp (hash-ref env (symbol->string arg1)))
  (define res (- tmp 1))
  (hash-set! env (symbol->string arg1) res)
)

(define (jnz arg1 arg2)
  (printf "jnz called ~a ~a\n" arg1 arg2)
)

;;(cpy 41 'a)
;;(cpy 'a 'b)
;;(inc 'a)
;;(dec 'a)
;;(println env)

;; hard coded the length here
;; only way i could get vectors
;; to work ha
(define (load-program )
  (define program (make-vector 23))
  (define pos 0)
  (define inf (open-input-file "input.txt"))
  (for ([l (in-lines inf)]) ;; loops the input
    (vector-set! program pos l) ;; save to vector
                                ;; in index pos
    (set! pos (+ pos 1))        ;; update pos++
  )
  (close-input-port inf)  ;; close the file
  program ;; return the vector
)

;; changed to return vector
;; need indexing for jnz
(define (load-program2)
  (define inf (open-input-file "input.txt"))
  (define tmp (sequence->list (in-lines inf))) ;; this is a sequence
  (close-input-port inf)  ;; close the file
  (list->vector tmp)
)

(define program (load-program2))
(printf "program is ~a\n" program)
