;; dotemacs
;; Location: /home/heitor/.emacs
;; Windows location: C:/Users/heitor/AppData/Roaming/.emacs
;; search "heitor" to find directory locations that need to be changed for the other operating system

;; for debugging in SBCL, save in ~/.sbclrc
;; (declaim (optimize (debug 3) (safety 3) (space 0) (speed 0)))
;; (format t "Debug optimized to 3")

;; (setq initial-scratch-message "My cool message,
;; Can be multi-line.
;; ")

;; quick-access function load a specific file
(defun quick-access-1 () (interactive) (find-file "/home/heitor/tmp/my-scratch.txt") (end-of-buffer))
(defun quick-access-C-f1 () (interactive) (find-file "/home/heitor/tmp/my-scratch.txt") (end-of-buffer))
(defun quick-access-4 () (interactive) (find-file "/home/heitor/mf-general/scrum/standup.txt"))
(defun quick-access-5 () (interactive) (find-file "/home/heitor/mf-general/notes/done.txt"))
(defun quick-access-7 () (interactive) (find-file "/home/heitor/code/reading-list/common-lisp-gentle-intro/notes.txt"))

(global-set-key (kbd "C-c f") 'fundamental-mode)
(global-set-key (kbd "C-c w") 'whitespace-mode)
(global-set-key (kbd "C-c C-l") 'find-file-literally)

(global-set-key (kbd "<f1>") 'quick-access-1)

(global-set-key (kbd "<C-f1>") 'quick-access-C-f1)
(global-set-key (kbd "<f2>") 'slime)
;; (global-set-key (kbd "<f2>") 'cider-jack-in)  ;; use in existing project folder

;; (global-set-key (kbd "<C-f2>") ; or C-f2
;;                 (lambda () (interactive) (progn (find-file-read-only "/home/heitor/cljrepl/project.clj")
;;                                                 (call-interactively 'cider-jack-in)))) ; works but leaves project.clj buffer open

(global-set-key (kbd "<f3>") 'isearch-forward)
(define-key isearch-mode-map (kbd "<f3>") 'isearch-repeat-forward)
(global-set-key (kbd "<f4>") 'load-diary)
(global-set-key (kbd "<f5>") 'run-python)
;; (global-set-key (kbd "<f6>") 'eval-last-sexp)
(global-set-key (kbd "<f7>") 'make-directory)
(global-set-key (kbd "<f8>") 'kill-this-buffer)
(global-set-key (kbd "<f9>") 'find-file-read-only)
(global-set-key (kbd "<C-f9>") 'find-file)
(global-set-key (kbd "<f10>") 'save-buffer)
(global-set-key (kbd "<f11>") 'write-file)
(global-set-key (kbd "<f12>") 'split-window-below)
(global-set-key (kbd "<C-f12>") 'split-window-right)

(global-set-key (kbd "<C-f3>") 'isearch-repeat-backward)
(global-set-key (kbd "<C-f4>") 'quick-access-4)
(global-set-key (kbd "<C-f5>") 'quick-access-5)
;; (global-set-key (kbd "<C-f5>") 'web-mode)
(global-set-key (kbd "<C-f6>") 'js-jsx-mode)
(global-set-key (kbd "<C-f7>") 'quick-access-7)

(setq default-directory "/home/heitor/")

;; window size and position
(setq initial-frame-alist '((top . 52) (left . 1420) (width . 79) (height . 88)))

(setq inhibit-startup-message t)
(setq backup-inhibited t)
(setq auto-save-default nil)
(setq make-backup-files nil)
(setq create-lockfiles nil)
(setq ring-bell-function 'ignore)
(setq split-width-threshold nil)  ;; prevent vertical split
(set-language-environment "UTF-8")
(setq-default frame-title-format "%f")
(delete-selection-mode t)
(menu-bar-mode -1)

(put 'downcase-region 'disabled nil)


;; avoid slowness with very long lines
;; (global-so-long-mode 1)

(require 'package)
(let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))
                    (not (gnutls-available-p))))
       (proto (if no-ssl "http" "https")))
  (when no-ssl
    (warn "\
Your version of Emacs does not support SSL connections,
which is unsafe because it allows man-in-the-middle attacks.
There are two things you can do about this warning:
1. Install an Emacs version that does support SSL and be safe.
2. Remove this warning from your init file so you won't see it again."))
  ;; Comment/uncomment these two lines to enable/disable MELPA and MELPA Stable as desired
  (add-to-list 'package-archives (cons "melpa" (concat proto "://melpa.org/packages/")) t)
  (add-to-list 'package-archives (cons "melpa-stable" (concat proto "://stable.melpa.org/packages/")) t)
  (when (< emacs-major-version 24)
    ;; For important compatibility libraries like cl-lib
    (add-to-list 'package-archives (cons "gnu" (concat proto "://elpa.gnu.org/packages/")))))

(package-initialize)

;; leim
;; (add-to-list 'load-path "/home/heitor/my-emacs/lisp/")
;; (require 'arabic-hc-v9)

(defun trim-string (string)
  "Remove white spaces in beginning and ending of STRING.
White space here is any of: space, tab, emacs newline (line feed, ASCII 10)."
  (replace-regexp-in-string "\\`[ \t\n]*" "" (replace-regexp-in-string "[ \t\n]*\\'" "" string)))

;; Custom
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["black" "red" "green" "yellow" "blue" "magenta" "cyan" "white"])
 '(c-basic-offset 4)
 '(c-default-style "linux")
 '(column-number-mode t)
 '(custom-enabled-themes (quote (my-tango)))
 '(custom-safe-themes
   (quote
    ("6ec8e3b1613810b66c9c39924b965115334983d188d9fbd1b59e75104ffc5155" "942ab00348cd0d4a24144ecacd7a3d7b9991bfa53989fc6a78db8ce23bf7a164" default)))
 '(default-tab-width 2 t)
 '(fill-column 72)
 '(global-visual-line-mode nil)
 '(indent-tabs-mode nil)
 '(ispell-personal-dictionary (expand-file-name "~/.aspell"))
 '(iswitchb-mode t)
 '(js-indent-level 2)
 '(package-selected-packages
   (quote
    (scala-mode rjsx-mode ## vlf js2-mode slime use-package isend-mode cider clojure-mode web-mode vue-html-mode ssass-mode pyvenv mmm-mode edit-indirect auto-complete)))
 '(py-closing-list-dedents-bos t)
 '(py-indent-list-style (quote line-up-with-first-element))
 '(py-install-directory "C:/Users/Tok/Desktop/code/")
 '(py-separator-char "/")
 '(savehist-mode t)
 '(scroll-conservatively 100)
 '(scroll-preserve-screen-position t)
 '(scroll-step 1)
 '(sql-db2-login-params nil)
 '(tool-bar-mode nil)
 '(web-mode-auto-close-style 1)
 '(web-mode-auto-quote-style 1)
 '(web-mode-block-padding 0)
 '(web-mode-code-indent-offset 2)
 '(web-mode-css-indent-offset 2)
 '(web-mode-enable-auto-closing t)
 '(web-mode-enable-auto-opening nil)
 '(web-mode-enable-auto-pairing nil)
 '(web-mode-enable-auto-quoting nil)
 '(web-mode-markup-indent-offset 2)
 '(web-mode-script-padding 0)
 '(web-mode-style-padding 0)
 '(yas/prompt-functions
   (quote
    (yas/ido-prompt yas/x-prompt yas/completing-prompt yas/no-prompt))))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.

 ;; Large font
 ;; '(default ((t (:inherit nil :stipple nil :background "PapayaWhip" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight light :height 100 :width normal :foundry "outline" :family "Liberation Mono")))))

 '(default ((t (:inherit nil :stipple nil :background "PapayaWhip" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight light :height 120 :width normal :foundry "outline" :family "ProggyTinyTTSZ")))))

;; auto-complete-mode
(require 'auto-complete-config)

(setq-default ac-sources (add-to-list 'ac-sources 'ac-source-dictionary))
(setq ac-disable-faces nil)

(global-auto-complete-mode t)
(setq ac-ignore-case nil)
(define-key ac-completing-map "\r" nil)  ; remove completion with RET
(setq ac-auto-start 1)
;; prevent pop-up on arrow keys
(define-key ac-completing-map (kbd "<down>") nil)
(define-key ac-completing-map (kbd "<up>") nil)
(setq ac-delay 0.0001)
(setq ac-disable-faces nil)
(setq ac-auto-show-menu 0.0001)

;; globals
(defun my-indent-whole-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'indent-region)))

(defun load-diary ()
  (interactive)
  (find-file "/home/heitor/mf-general/notes/general.txt"))

;; C-<backspace> does not add to kill ring
(defun backward-delete-word (arg)
  (interactive "p")
  (delete-region (point) (progn (backward-word arg) (point))))

;; C-<delete> does not add to kill ring
(defun forward-delete-word (arg)
  (interactive "p")
  (delete-region (point) (progn (forward-word arg) (point))))

(global-set-key (kbd "C-<backspace>") 'backward-delete-word)
(global-set-key (kbd "C-<delete>") 'forward-delete-word)

(global-set-key (kbd "M-<backspace>") 'backward-delete-word)
(global-set-key (kbd "M-<delete>") 'forward-delete-word)

(global-set-key (kbd "<M-left>") 'backward-sexp)
(global-set-key (kbd "<M-right>") 'forward-sexp)
(global-set-key (kbd "C-M-<backspace>") 'backward-kill-sexp)

(global-set-key (kbd "C-t") 'yank)
(global-set-key (kbd "M-t") 'yank-pop)
(global-set-key (kbd "M-k") 'jpk/delete-line)

(global-set-key (kbd "RET") 'newline-and-indent)

(global-set-key (kbd "C-<") 'previous-buffer)
(global-set-key (kbd "C->") 'next-buffer)
(global-set-key (kbd "C-'") 'switch-to-buffer)

(global-set-key (kbd "C-c C-a") 'auto-complete-mode)

(global-set-key (kbd "<M-up>") 'previous-multiframe-window)
(global-set-key (kbd "<M-down>") 'next-multiframe-window)
(global-set-key (kbd "M-o") 'other-window)

(global-set-key (kbd "M-p") 'backward-paragraph)
(global-set-key (kbd "M-n") 'forward-paragraph)

(global-set-key (kbd "C-c C-e") 'electric-indent-mode)
(global-set-key (kbd "C-c i") 'indent-region)

(global-set-key (kbd "M-w") 'kill-ring-save)
(global-set-key (kbd "M-u") 'undo)
(global-set-key (kbd "C-z") 'undo)

(global-set-key (kbd "C-x x") 'copy-line)
(global-set-key (kbd "C-/") 'sgml-close-tag)

;; cursor
(blink-cursor-mode 1)
(set-cursor-color "#337c10")

;; box cursor
(set-default 'cursor-type 'box)

;; bar cursor
;; (set-default 'cursor-type 'bar)

;; force regular font
(defun disable-bold ()
  (interactive)
  (mapc (lambda (face) (set-face-attribute face nil :weight 'normal :underline nil)) (face-list)))
(call-interactively 'disable-bold)

(set-face-bold-p 'bold nil)

(defun remap-faces-default-attributes ()
  (let ((family (face-attribute 'default :family))
        (height (face-attribute 'default :height)))
    (mapcar (lambda (face)
              (face-remap-add-relative
               face :family family :weight 'normal :height height))
          (face-list))))

(when (display-graphic-p)
  (add-hook 'minibuffer-setup-hook 'remap-faces-default-attributes)
  (add-hook 'change-major-mode-after-body-hook 'remap-faces-default-attributes))

(electric-indent-mode t)
(add-hook 'python-mode-hook
          (lambda () (set (make-local-variable 'electric-indent-mode) nil)))  ; disable electric indent for python

;; custom functions
;; general
(defun line-emptyp ()
  (= (line-beginning-position) (line-end-position)))

(defun copy-line ()
  (interactive)
  (beginning-of-line)
  (kill-line)
  (yank))

;; Python
;; Inferior Python and testing
(setq python-shell-interpreter "/home/heitor/bin/python3.10")

(setenv "PYTHONPATH" "/home/heitor/code/shared/python/my-modules:/home/heitor/tok_data")
(setenv "PYTHONSTARTUP" "/home/heitor/code/shared/python/mystartup.py")
(setenv "PYTHONUNBUFFERED" "x")
(setenv "PYTHONIOENCODING" "utf8")

;; .mysecrets contains:
;;
;; export TOKAPI_PREV_PONTUAL_API_TOKEN='myapitoken'
;; export TOKAPI_PREV_PONTUAL_BEL_PASSWORD='belpassword'
;; etc.

(setenv "TOKAPI_PREV_PONTUAL_API_TOKEN" (shell-command-to-string ". ~/.mysecrets; echo -n $TOKAPI_PREV_PONTUAL_API_TOKEN"))
(setenv "TOKAPI_PREV_PONTUAL_BEL_USERNAME" "tempo-ok-pf")
(setenv "TOKAPI_PREV_PONTUAL_BEL_PASSWORD" (shell-command-to-string ". ~/.mysecrets; echo -n $TOKAPI_PREV_PONTUAL_BEL_PASSWORD"))
(setenv "ECCODES_DIR" "/home/heitor")
(setenv "TOKENEL_DB_PASSWORD" (shell-command-to-string ". ~/.mysecrets; echo -n $TOKENEL_DB_PASSWORD"))

;; suppress Python shell warning
(setq python-shell-completion-native-disabled-interpreters '("python"))

;; closing bracket after multi-line definition should line up with original
;; https://stackoverflow.com/questions/4293074/in-emacs-python-mode-customize-multi-line-statement-indentation

(defadvice python-calculate-indentation (around outdent-closing-brackets)
  "Handle lines beginning with a closing bracket and indent them so that
they line up with the line containing the corresponding opening bracket."
  (save-excursion
    (beginning-of-line)
    (let ((syntax (syntax-ppss)))
      (if (and (not (eq 'string (syntax-ppss-context syntax)))
               (python-continuation-line-p)
               (cadr syntax)
               (skip-syntax-forward "-")
               (looking-at "\\s)"))
          (progn
            (forward-char 1)
            (ignore-errors (backward-sexp))
            (setq ad-return-value (current-indentation)))
        ad-do-it))))
(ad-activate 'python-calculate-indentation)

(defun my-python-send-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (trim-string (buffer-string)))))

(defun my-python-print-and-send-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (concat "print('''" (trim-string (buffer-string)) "''')"))
    (python-shell-send-string (concat "print('')\n" (trim-string (buffer-string))))))

(defun my-python-send-statement ()
  (interactive)
  ;; (local-set-key [S-return] 'my-python-send-statement)
  (python-shell-send-string (thing-at-point 'line))
  (python-shell-send-string "\n")
  (move-end-of-line nil))

(defun my-python-send-block ()
  (interactive)
  (set-mark (line-end-position))
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'python-shell-send-region)
    (python-shell-send-string "\n")
    (dotimes (i lines-of-block)
      (next-line))
    (end-of-line)))

(defun my-js-send-block ()
  (interactive)
  (set-mark (line-end-position))
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'js-send-region)
    (dotimes (i lines-of-block)
      (next-line))
    (end-of-line)))

(defun my-js-send-line ()
  (interactive)
  (set-mark (line-end-position))
  (beginning-of-line)
  (call-interactively 'js-send-region)
  (end-of-line))

;; isend-mode
(defun my-isend-send-sexp ()
  (interactive)
  (save-excursion
    (backward-sexp)
    (mark-sexp)
    (call-interactively 'isend-send)))

(defun my-isend-send-line ()
  (interactive)
  (set-mark (line-end-position))
  (beginning-of-line)
  (call-interactively 'isend-send)
  (end-of-line))

(defun my-isend-send-block ()
  (interactive)
  (set-mark (line-end-position))
  (let ((lines-of-block 0))
    (while (or (equal (line-beginning-position) 0) (not (line-emptyp)))
      (previous-line)
      (beginning-of-line)
      (set 'lines-of-block (+ 1 lines-of-block)))
    (beginning-of-line)
    (call-interactively 'isend-send)
    (end-of-line)))

;; (setq scheme-program-name "/usr/local/bin/mit-scheme --load /home/heitor/code/shared/scheme/heitor.scm")
(setq scheme-program-name "/home/heitor/bin/csi -:c")

(defun my-scheme-send-buffer ()
  (interactive)
  (mark-whole-buffer)
  (call-interactively 'scheme-send-region)
  (end-of-buffer)
  (deactivate-mark))

(setq inferior-lisp-program "/usr/bin/sbcl")

(defun my-lisp-send-buffer ()
  (interactive)
  (save-excursion
    (mark-whole-buffer)
    (call-interactively 'lisp-eval-region)
    (deactivate-mark)
    (end-of-buffer)))

(add-hook 'isend-mode-hook
          (lambda ()
            (define-key isend-mode-map (kbd "<C-return>") 'isend-send-buffer)))  ;; override default

(add-hook 'emacs-lisp-mode-hook
          (lambda ()
            (local-set-key (kbd "<M-left>") 'backward-sexp)
            (local-set-key (kbd "<M-right>") 'forward-sexp)
            (local-set-key [S-return] (lambda () (interactive) (call-interactively 'eval-print-last-sexp) (insert "\n")))))

(add-hook 'lisp-mode-hook
          (lambda ()
            (local-set-key (kbd "<M-left>") 'backward-sexp)
            (local-set-key (kbd "<M-right>") 'forward-sexp)
            (local-set-key [C-return] 'slime-eval-buffer)
            (local-set-key [S-return] 'slime-eval-last-expression)))

(add-hook 'slime-repl-mode-hook
          (lambda ()
            (auto-complete-mode 0)
            (local-set-key (kbd "C-c C-q") 'slime-repl-quit)))

(add-hook 'scheme-mode-hook
          (lambda ()
            (local-set-key [C-return] 'my-scheme-send-buffer)
            (local-set-key [S-return] 'scheme-send-last-sexp)))

(add-hook 'shell-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(defun my-cider-save-and-compile-buffer ()
  (interactive)
  (call-interactively 'save-buffer)
  (call-interactively 'cider-load-buffer))

(defun my-cider-save-and-eval-buffer ()
  (interactive)
  (call-interactively 'save-buffer)
  (call-interactively 'cider-eval-buffer))

(setq cider-repl-display-help-banner nil)
(add-hook 'clojure-mode-hook
          (lambda ()
            (auto-complete-mode 1)
            (define-key clojure-mode-map (kbd "<M-left>") 'backward-sexp)
            (define-key clojure-mode-map (kbd "<M-right>") 'forward-sexp)
            (define-key clojure-mode-map (kbd "<S-return>") 'cider-eval-defun-at-point)
            (define-key clojure-mode-map (kbd "<C-return>") 'my-cider-save-and-eval-buffer)))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c C-c") 'keyboard-escape-quit)
            (local-set-key (kbd "C-c c") 'comment-region)
            (local-set-key (kbd "C-c u") 'uncomment-region)
            (local-set-key (kbd "RET") 'newline-and-indent)
            (local-set-key (kbd "C-c l") (lambda () (interactive) (insert "# debug\nprint(")))
            (local-set-key [S-return] 'my-python-send-statement)
            (local-set-key [M-return] (lambda () (interactive) (progn (call-interactively 'python-shell-send-region) (deactivate-mark))))
            (local-set-key [C-return] 'my-python-send-buffer)))

(add-hook 'web-mode-hook
          (lambda ()
            ;;; indent spaces
            (setq indent-tabs-mode nil)

            ;;; indent tabs
	    ;; (setq indent-tabs-mode t) (setq tab-width 2) (web-mode-use-tabs)

            (local-set-key (kbd "C-c l") (lambda () (interactive) (insert "// debug\n  console.log(")))))

(add-hook 'before-save-hook 'delete-trailing-whitespace)

(add-hook 'js-mode-hook
          (lambda ()
            (local-set-key (kbd "C-c c") 'js-send-buffer)
            (local-set-key [S-return] 'my-js-send-line)
            (local-set-key [C-return] 'my-js-send-block)))

(add-hook 'rjsx-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'html-mode-hook
          (lambda ()
            (auto-complete-mode 1)
            (sgml-mode)
            (js-jsx-mode)))

(with-eval-after-load 'rjsx-mode
  (define-key rjsx-mode-map "<" nil)
  (define-key rjsx-mode-map (kbd "C-d") nil)
  (define-key rjsx-mode-map ">" nil))

(add-to-list 'auto-mode-alist '("\\.php\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.vue\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.html\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.js\\'" . web-mode))

;; text mode
(add-hook 'text-mode-hook
          (lambda ()
            (setq indent-tabs-mode t)
            (auto-complete-mode 1)))

(define-key text-mode-map (kbd "TAB") 'self-insert-command)
(define-key text-mode-map [backtab] 'indent-for-tab-command)

(add-hook 'sql-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'inferior-scheme-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'inferior-lisp-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'inferior-python-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(add-hook 'cider-repl-mode-hook
          (lambda ()
            (auto-complete-mode 1)))

(put 'upcase-region 'disabled nil)

;; Foreign languages input
(defun get-greek-entry ()
  (interactive)

  (activate-input-method "portuguese-prefix")
  (insert
   (read-string "Portugues: " nil nil nil t))

  (insert "\n")
  (activate-input-method "greek")
  (insert
   (read-string "ELLINIKA: " nil nil nil t))

  (insert "\n\n")
  (get-greek-entry))

;; swap input methods in buffer
(defun my-greek-swap-input-methods ()
  (interactive)
  (if (equal current-input-method "greek")
      (activate-input-method "portuguese-prefix")
    (activate-input-method "greek")))

;; Custom insert strings
(defun insert-my-custom-string ()
  (interactive)
  (insert "My custom string"))

(setq default-input-method "portuguese-prefix")

;; delete without adding to kill ring
(defmacro jpk/delete-instead-of-kill (&rest body)
  "Replaces `kill-region' with `delete-region' in BODY."
  `(cl-letf (((symbol-function 'kill-region)
              (lambda (beg end &optional yank-handler)
                (delete-region beg end))))
     ,@body))

(defun jpk/delete-line (arg)
  "Like `kill-line', but does not save to the `kill-ring'."
  (interactive "*p")
  (jpk/delete-instead-of-kill (kill-line arg)))

;; close all parens, from emacs stackexchange
;; Note: case was replaced with cl-case

(defun close-all-parentheses ()
  (interactive "*")
  (let ((closing nil))
    (save-excursion
      (while (condition-case nil
         (progn
           (backward-up-list)
           (let ((syntax (syntax-after (point))))
             (cl-case (car syntax)
               ((4) (setq closing (cons (cdr syntax) closing)))
               ((7 8) (setq closing (cons (char-after (point)) closing)))))
           t)
           ((scan-error) nil))))
    (apply #'insert (nreverse closing))))

(global-set-key (kbd "M-)") 'close-all-parentheses)

;; line-by-line block editing functions

(setq myval "")

(defun my-read ()
  (interactive)
  (setq myval (read-string (concat "Enter value to save in myval: "))))

(defun my-lines (transformation)
  (let ((lines (split-string (string-trim myval) "\n")))
    (insert (concat "\n" (string-join (mapcar transformation lines) "\n") "\n"))))

;; usage: (my-lines 'my-sql-value)
;;        (my-lines 'my-split-commas)
(defun my-sql-value (line)
  (concat "(" (replace-regexp-in-string "\"" "'" line) ")," ))

(defun my-split-commas (line)
  (insert (replace-regexp-in-string "," "\n" line) "\n"))

;; move to last sexp
(defun jump-to-last-sexp ()
  (interactive)
  (let ((pt (point))
        (fwpt (progn
                (thing-at-point--end-of-sexp) (point))))
    (while (not (eq pt fwpt))
      (setq pt fwpt fwpt (progn (thing-at-point--end-of-sexp) (point))))))

(global-set-key (kbd "M-e") 'jump-to-last-sexp)

;; beginning-of-sexp is unpredictable because when cursor is at (|value1 value2 value3)
;; calling beginning-of-sexp will move the cursor outside the sexp.
(defun jump-to-first-sexp ()
  (interactive)
  (let ((pt (point))
        (bkpt (progn
                (thing-at-point--beginning-of-sexp) (point))))
    (while (not (eq pt bkpt))
      (setq pt bkpt bkpt (progn (thing-at-point--beginning-of-sexp) (point))))))

(global-set-key (kbd "M-a") 'jump-to-first-sexp)
