"""
You recently started freelance software development and have been offered a variety of job opportunities. Each job has a deadline, meaning there is no value in completing the work after the deadline. Additionally, each job has an associated payment representing the profit for completing that job. Given this information, write a function that returns the maximum profit that can be obtained in a 7-day period.

Each job will take 1 full day to complete, and the deadline will be given as the number of days left to complete the job. For example, if a job has a deadline of 1, then it can only be completed if it is the first job worked on. If a job has a deadline of 2, then it could be started on the first or second day.

Note: There is no requirement to complete all of the jobs. Only one job can be worked on at a time, meaning that in some scenarios it will be impossible to complete them all.
"""

def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: (job['payment']), reverse=True)
    number_of_days = 7
    result = [0] * number_of_days
    for job in jobs:
        deadline = min(number_of_days, job['deadline'])
        if not result[deadline - 1] or result[deadline - 1] < job['payment']:
            result[deadline - 1] = job['payment']
            continue
        for check in range(deadline - 2, -1, -1):
            if not result[check] or result[check] < job['payment']:
                result[check] = job['payment']
                break
    return sum(result)

"""
Time Complexity: O(nlogn); Space Complexity: O(7) = O(1)
The time complexity is O(nlogn) where n is the number of jobs in the input list.
The space complexity is O(1) since we are using a fixed-size array of length 7 to store the maximum payment for each day.

The idea is to sort the jobs in descending order based on their payment. This way, we can prioritize the jobs with the highest payment first. We assign each job to the latest possible day before its deadline. 
If the job's payment is greater than the payment for that day, we update the payment for that day. If the payment for that day is already greater than the job's payment, we move to the previous day and check if the payment for that day is less than the job's payment. 
We continue this process until we find a day with a lower payment or reach the first day. Finally, we sum up the payments for each day to get the maximum profit that can be obtained in a 7-day period.
"""