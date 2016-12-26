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

(cpy 41 'a)
(cpy 'a 'b)
(inc 'a)
(dec 'a)
(println env)
