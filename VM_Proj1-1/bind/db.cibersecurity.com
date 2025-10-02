$TTL	604800
$ORIGIN	cibersecurity.com.
@	IN	SOA	ns1.cibersecurity.com.	admin.cibersecurity.com.	(
			2022123001	; Serial
			604800		; Refresh
			86400		; Retry
			2419200		; Expire
			604800)		; Negative Cache TTL
	IN	NS	ns1.cibersecurity.com.
ns1	IN	A	120.100.20.100
@	IN	A	120.100.20.100
www	IN	A	120.100.20.100
