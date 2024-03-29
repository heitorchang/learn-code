;; save in ~/.emacs.d/

(deftheme my-tango
  "Created 2020-11-16.")

(custom-theme-set-faces
 'my-tango
 '(default ((t (:family "ProggyTinyTTSZ" :foundry "unknown" :width normal :height 120 :weight normal :slant normal :underline nil :overline nil :strike-through nil :box nil :inverse-video nil :foreground "black" :background "PapayaWhip" :stipple nil :inherit nil))))
 '(cursor ((t (:background "#204a87"))))
 '(fixed-pitch ((t (:family "Monospace" :weight normal :underline nil))))
 '(variable-pitch ((t (:family "Sans Serif" :weight normal :underline nil))))
 '(escape-glyph ((t (:foreground "#a40000"))))
 '(homoglyph ((t (:foreground "#a40000"))))
 '(minibuffer-prompt ((t (:weight bold :foreground "#204a87"))))
 '(highlight ((t (:background "powder blue"))))
 '(region ((t (:background "powder blue"))))
 '(shadow ((t (:weight normal :underline nil :foreground "grey50"))))
 '(secondary-selection ((t (:background "#8cc4ff"))))
 '(trailing-whitespace ((t (:background "#ef2929"))))
 '(font-lock-builtin-face ((t (:foreground "#75507b"))))
 '(font-lock-comment-delimiter-face ((t (:weight normal :underline nil :inherit (font-lock-comment-face)))))
 '(font-lock-comment-face ((t (:slant italic :foreground "#5f615c"))))
 '(font-lock-constant-face ((t (:weight bold :foreground "#204a87"))))
 '(font-lock-doc-face ((t (:weight normal :underline nil :inherit (font-lock-string-face)))))
 '(font-lock-function-name-face ((t (:foreground "#a40000"))))
 '(font-lock-keyword-face ((t (:foreground "#346604"))))
 '(font-lock-negation-char-face ((t (:weight normal :underline nil))))
 '(font-lock-preprocessor-face ((t (:weight normal :underline nil :inherit (font-lock-builtin-face)))))
 '(font-lock-regexp-grouping-backslash ((t (:weight normal :underline nil :inherit (bold)))))
 '(font-lock-regexp-grouping-construct ((t (:weight normal :underline nil :inherit (bold)))))
 '(font-lock-string-face ((t (:foreground "#5c3566"))))
 '(font-lock-type-face ((t (:foreground "#204a87"))))
 '(font-lock-variable-name-face ((t (:foreground "#b35000"))))
 '(font-lock-warning-face ((t (:weight normal :underline nil :inherit (error)))))
 '(button ((t (:weight normal :underline nil :inherit (link)))))
 '(link ((t (:underline (:color foreground-color :style line) :foreground "#204a87"))))
 '(link-visited ((t (:underline (:color foreground-color :style line) :foreground "#3465a4"))))
 '(fringe ((t (:background "#d3d7cf"))))
 '(header-line ((t (:weight normal :underline nil :box nil :foreground "grey20" :background "grey90" :inherit (mode-line)))))
 '(tooltip ((t (:weight normal :underline nil :foreground "black" :background "lightyellow" :inherit (variable-pitch)))))
 '(mode-line ((t (:box (:line-width -1 :color nil :style released-button) :foreground "#2e3436" :background "#d3d7cf"))))
 '(mode-line-buffer-id ((t (:weight normal :underline nil))))
 '(mode-line-emphasis ((t (:weight normal :underline nil))))
 '(mode-line-highlight ((t (:weight normal :underline nil :box (:line-width 2 :color "grey40" :style released-button)))))
 '(mode-line-inactive ((t (:box (:line-width -1 :color nil :style released-button) :foreground "#2e3436" :background "#888a85"))))
 '(isearch ((t (:foreground "#ffffff" :background "#ce5c00"))))
 '(isearch-fail ((t (:weight normal :underline nil :background "RosyBrown1"))))
 '(lazy-highlight ((t (:background "#e9b96e"))))
 '(match ((t (:weight normal :underline nil :background "yellow1"))))
 '(next-error ((t (:weight normal :underline nil :inherit (region)))))
 '(query-replace ((t (:weight normal :underline nil :inherit (isearch))))))

(provide-theme 'my-tango)
