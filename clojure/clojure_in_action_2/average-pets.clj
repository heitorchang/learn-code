(defn average-pets [users]
  (let [user-data (vals users)
        pet-counts (map :number-pets user-data)
        _ (println "total pets:" pet-counts)  ; use this awful style in debugging only
        total (apply + pet-counts)
        _ (println "total:" total)]
    (/ total (count users) 1.0)))


(average-pets {:john {:number-pets 6}
               :sara {:number-pets 2}
               :jack {:number-pets 0}})
