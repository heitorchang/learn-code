// Also times out

class Node {
    public String resta;
    public String restb;
    public String accum;
        
    public Node(String iresta, String irestb, String iaccum) {
        resta = iresta;
        restb = irestb;
        accum = iaccum;
    }
    
    public String getAccum() {
        return this.accum;
    }
    
    public String getA() {
        return this.resta;
    }
    
    public String getB() {
        return this.restb;
    }
    
    public int cmp(Node other) {
        char tlast = this.accum.charAt(this.accum.length() - 1);
        char olast = other.accum.charAt(other.accum.length() - 1);
        if (tlast == olast) {
            return 0;
        }
        if (tlast < olast) {
            return -1;
        }
        return 1;
    }
        
}

String step(Node n) {
    if (n.getA().equals("") && n.getB().equals("")) {
        return n.getAccum();
    }
    
    if (n.getA().equals("")) {
        return n.getAccum() + n.getB();
    }
    
    if (n.getB().equals("")) {
        return n.getAccum() + n.getA();
    }
    
    Node left = new Node(n.getA().substring(1), n.getB(), n.getAccum() + n.getA().substring(0, 1));
    Node right = new Node(n.getA(), n.getB().substring(1), n.getAccum() + n.getB().substring(0, 1));
    
    int lcmp = left.cmp(right);
    if (lcmp == -1) {
        return step(left);
    }
    if (lcmp == 1) {
        return step(right);
    }
    return Math.min(step(left).compareTo(step(right)));
}


String theSmallestStringCipher(String key, String message) {
    return step(new Node(key, message, ""));
}


