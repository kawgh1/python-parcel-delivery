class HashMap:
    # Constructor
    # Space-time complexity is O(1)
    def __init__(self):
        self.size = 100
        # self.map = [None] * self.size changed on 5-23-2020
        self.map = [None] * self.size

    # private getter to create hash key
    # Space-time complexity is O(1)
    def _get_hash(self, key):

        # ord(x) returns the Unicode integer value of string 'x'
        hash = int(key) % self.size
        return hash

    # Space-time complexity is O(N)
    def add(self, key, value):

        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list(key_value)
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            self.map[key_hash].append(key_value)
            return True

    # Space-time complexity is O(N)
    def get(self, key):

        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            return self.map[key_hash][1]

            # for pair in self.map[key_hash]:
            #     if pair[0] == key:
            #         return pair[1]


            # for item in self.map:
            #     if item[0] == key:
            #         return item[1]

        return None

    # Space-time complexity is O(N)
    def delete(self, key):

        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # Space-time complexity is O(N)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error updating key: ' + key)

    # Space-time complexity is O(N)
    def printHashMap(self):
        print('----Hash Map----')
        for item in self.map:
            if item is not None:
                print(str(item))
