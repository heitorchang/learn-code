fun solution(year: Int): Int {
  // 1700 = 17  1699  1701
  // 1701 = 18  1700  1702
  // subtract 1 then divide by 100
  // this way, 1700 and 1701 will be treated differently
  // adding 1 will only make them the same
  return ((year - 1) / 100) + 1
}
