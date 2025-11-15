; Time-stamp: <2025-11-15 18:17:14>
; simply add the following elisp code to your emacs configuration to obtain the org-dblp interactive function


;!SECTION! orgDBLP_query wrapper 
; Make sure to modify the path to the =orgDBLP_query= executable as needed

(defun org-dblp(query url)
  (interactive
   (list
    (read-string "query:")
    (read-string "open URL:")))
  (with-current-buffer
      (switch-to-buffer "org-dblp")
    (org-mode)
    (end-of-buffer)
    (insert (shell-command-to-string
             (format
              "~/.local/bin/orgDBLP_query -u \"%s\" -q \"%s\"" ; <-- !TODO! update this path
              url
              query)))))


;!SECTION! org-roam functions


(defun pi2-6-org-roam-find-paper ()
  (interactive)
  (org-roam-node-find
   nil nil
   (lambda (node)
     (member "paper" (org-roam-node-tags node)))))


(defun pi2-6-org-roam-find-not-paper ()
  (interactive)
  (org-roam-node-find
   nil nil
   (lambda (node)
     (not (member "paper" (org-roam-node-tags node))))))





