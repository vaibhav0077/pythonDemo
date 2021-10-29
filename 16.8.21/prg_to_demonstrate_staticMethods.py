try:
    class timerableOfWeeklydays:
        
        @staticmethod
        def timee(day):
            if day == "sunday":
                return "Holiday"
            else:
                return "open"
       
    
    day = str(input("Enter A day : "))

    print(timerableOfWeeklydays.timee(day))

except Exception as e:

    print(e)


