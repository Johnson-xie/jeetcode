func minSteps(s string, t string) int {

    count := 0

    arr := [26]int{}

    for i := 0; i < len(s); i++ {
        arr[s[i] - 'a']++
        arr[t[i] - 'a']--
    }

    for _, value := range arr {
        if value > 0 {
            count += value
        }
    }

    return count


}