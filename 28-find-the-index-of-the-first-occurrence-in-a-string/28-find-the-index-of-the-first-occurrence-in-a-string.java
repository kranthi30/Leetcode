class Solution {
    public int strStr(String haystack, String needle) {
  int hlen=haystack.length();
    int nlen=needle.length();
    if(nlen==0)
        return 0;
    if(nlen>hlen)
        return -1;
    if(nlen==hlen && haystack.equals(needle))
        return 0;
    for(int i=0;i<=hlen-nlen;i++)
    {
        String subStr=haystack.substring(i,i+nlen);
        if(needle.equals(subStr))
            return i;
    }
    return -1;
}
}