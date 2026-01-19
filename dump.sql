--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Debian 16.4-1.pgdg110+2)
-- Dumped by pg_dump version 16.4 (Debian 16.4-1.pgdg110+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: tiger; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA tiger;


ALTER SCHEMA tiger OWNER TO postgres;

--
-- Name: tiger_data; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA tiger_data;


ALTER SCHEMA tiger_data OWNER TO postgres;

--
-- Name: topology; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA topology;


ALTER SCHEMA topology OWNER TO postgres;

--
-- Name: SCHEMA topology; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA topology IS 'PostGIS Topology schema';


--
-- Name: fuzzystrmatch; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;


--
-- Name: EXTENSION fuzzystrmatch; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


--
-- Name: postgis_tiger_geocoder; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder WITH SCHEMA tiger;


--
-- Name: EXTENSION postgis_tiger_geocoder; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis_tiger_geocoder IS 'PostGIS tiger geocoder and reverse geocoder';


--
-- Name: postgis_topology; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis_topology WITH SCHEMA topology;


--
-- Name: EXTENSION postgis_topology; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis_topology IS 'PostGIS topology spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: activity; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.activity (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    parent_id integer
);


ALTER TABLE public.activity OWNER TO postgres;

--
-- Name: activity_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.activity_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.activity_id_seq OWNER TO postgres;

--
-- Name: activity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.activity_id_seq OWNED BY public.activity.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: building; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.building (
    id integer NOT NULL,
    address character varying(255) NOT NULL,
    location public.geometry(Point,4326) NOT NULL
);


ALTER TABLE public.building OWNER TO postgres;

--
-- Name: building_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.building_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.building_id_seq OWNER TO postgres;

--
-- Name: building_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.building_id_seq OWNED BY public.building.id;


--
-- Name: organization; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.organization (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    building_id integer NOT NULL
);


ALTER TABLE public.organization OWNER TO postgres;

--
-- Name: organization_activity; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.organization_activity (
    organization_id integer NOT NULL,
    activity_id integer NOT NULL
);


ALTER TABLE public.organization_activity OWNER TO postgres;

--
-- Name: organization_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.organization_id_seq OWNER TO postgres;

--
-- Name: organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.organization_id_seq OWNED BY public.organization.id;


--
-- Name: phone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.phone (
    id integer NOT NULL,
    number character varying(32) NOT NULL,
    organization_id integer NOT NULL
);


ALTER TABLE public.phone OWNER TO postgres;

--
-- Name: phone_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.phone_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.phone_id_seq OWNER TO postgres;

--
-- Name: phone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.phone_id_seq OWNED BY public.phone.id;


--
-- Name: activity id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activity ALTER COLUMN id SET DEFAULT nextval('public.activity_id_seq'::regclass);


--
-- Name: building id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.building ALTER COLUMN id SET DEFAULT nextval('public.building_id_seq'::regclass);


--
-- Name: organization id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organization ALTER COLUMN id SET DEFAULT nextval('public.organization_id_seq'::regclass);


--
-- Name: phone id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone ALTER COLUMN id SET DEFAULT nextval('public.phone_id_seq'::regclass);


--
-- Data for Name: activity; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.activity (id, name, parent_id) FROM stdin;
1	Еда	\N
2	Автомобили	\N
3	Услуги	\N
4	Мясная продукция	1
5	Молочная продукция	1
6	Фастфуд	1
7	Легковые	2
8	Грузовые	2
9	Ремонт	3
10	Обучение	3
11	Стейки	4
12	Колбасы	4
13	Сыры	5
14	Школы вождения	10
15	Автосервисы	9
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
049ce7da6415
\.


--
-- Data for Name: building; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.building (id, address, location) FROM stdin;
1	Москва, Тверская 1	0101000020E6100000AE47E17A14CE4240E17A14AE47E14B40
2	Москва, Арбат 12	0101000020E610000016FBCBEEC9CB4240C74B378941E04B40
3	Москва, Ленинградский пр-т 15	0101000020E61000001C7C613255C8424079E9263108E44B40
4	Москва, Кутузовский 24	0101000020E6100000226C787AA5C44240105839B4C8DE4B40
5	Москва, Садовая 7	0101000020E6100000BADA8AFD65CF4240E02D90A0F8E14B40
6	Москва, Пресненская наб. 8	0101000020E610000069006F8104C5424039454772F9DF4B40
7	Москва, Бауманская 5	0101000020E6100000AD69DE718AD64240FB5C6DC5FEE24B40
8	Москва, Профсоюзная 22	0101000020E6100000ABCFD556ECC7424092CB7F48BFD54B40
9	Москва, Щёлковское ш. 3	0101000020E6100000CA32C4B12EE642402BF697DD93E74B40
10	Москва, Варшавское ш. 10	0101000020E61000000F0BB5A679CF424088855AD3BCD34B40
11	Москва, Новослободская 19	0101000020E61000003108AC1C5ACC42404ED1915CFEE34B40
12	Москва, Павелецкая пл. 1	0101000020E6100000A8C64B3789D1424077BE9F1A2FDD4B40
13	Москва, Маросейка 9	0101000020E610000045D8F0F44AD1424054742497FFE04B40
14	Москва, Ярославское ш. 6	0101000020E6100000C0EC9E3C2CDC4240CDCCCCCCCCEC4B40
15	Москва, Рязанский пр-т 18	0101000020E6100000E63FA4DFBEDE4240C05B2041F1DB4B40
\.


--
-- Data for Name: organization; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.organization (id, name, building_id) FROM stdin;
1	ООО Мясной Дом	1
2	ИП Молоко+	2
3	Burger House	3
4	АвтоМир	4
5	Truck Service	5
6	РемБыт	6
7	Drive School	7
8	Cheese Club	8
9	Steak & Co	9
10	Колбасный Рай	10
11	Fast&Good	11
12	AutoFix	12
13	Учебный Центр Профи	13
14	Грузовой Сервис	14
15	Молочная Лавка	15
\.


--
-- Data for Name: organization_activity; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.organization_activity (organization_id, activity_id) FROM stdin;
1	4
1	11
2	5
2	13
3	6
4	7
5	8
6	9
6	15
7	14
8	13
9	11
10	12
11	6
12	15
13	10
14	8
15	5
\.


--
-- Data for Name: phone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.phone (id, number, organization_id) FROM stdin;
1	8-900-000-0001	1
2	8-900-000-0002	2
3	8-900-000-0003	3
4	8-900-000-0004	4
5	8-900-000-0005	5
6	8-900-000-0006	6
7	8-900-000-0007	7
8	8-900-000-0008	8
9	8-900-000-0009	9
10	8-900-000-0010	10
11	8-900-000-0011	11
12	8-900-000-0012	12
13	8-900-000-0013	13
14	8-900-000-0014	14
15	8-900-000-0015	15
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: geocode_settings; Type: TABLE DATA; Schema: tiger; Owner: postgres
--

COPY tiger.geocode_settings (name, setting, unit, category, short_desc) FROM stdin;
\.


--
-- Data for Name: pagc_gaz; Type: TABLE DATA; Schema: tiger; Owner: postgres
--

COPY tiger.pagc_gaz (id, seq, word, stdword, token, is_custom) FROM stdin;
\.


--
-- Data for Name: pagc_lex; Type: TABLE DATA; Schema: tiger; Owner: postgres
--

COPY tiger.pagc_lex (id, seq, word, stdword, token, is_custom) FROM stdin;
\.


--
-- Data for Name: pagc_rules; Type: TABLE DATA; Schema: tiger; Owner: postgres
--

COPY tiger.pagc_rules (id, rule, is_custom) FROM stdin;
\.


--
-- Data for Name: topology; Type: TABLE DATA; Schema: topology; Owner: postgres
--

COPY topology.topology (id, name, srid, "precision", hasz) FROM stdin;
\.


--
-- Data for Name: layer; Type: TABLE DATA; Schema: topology; Owner: postgres
--

COPY topology.layer (topology_id, layer_id, schema_name, table_name, feature_column, feature_type, level, child_id) FROM stdin;
\.


--
-- Name: activity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.activity_id_seq', 1, false);


--
-- Name: building_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.building_id_seq', 1, false);


--
-- Name: organization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.organization_id_seq', 1, false);


--
-- Name: phone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.phone_id_seq', 1, false);


--
-- Name: topology_id_seq; Type: SEQUENCE SET; Schema: topology; Owner: postgres
--

SELECT pg_catalog.setval('topology.topology_id_seq', 1, false);


--
-- Name: activity activity_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activity
    ADD CONSTRAINT activity_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: building building_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.building
    ADD CONSTRAINT building_pkey PRIMARY KEY (id);


--
-- Name: organization_activity organization_activity_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organization_activity
    ADD CONSTRAINT organization_activity_pkey PRIMARY KEY (organization_id, activity_id);


--
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (id);


--
-- Name: phone phone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone
    ADD CONSTRAINT phone_pkey PRIMARY KEY (id);


--
-- Name: activity uq_activity_parent_name; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activity
    ADD CONSTRAINT uq_activity_parent_name UNIQUE (parent_id, name);


--
-- Name: phone uq_phone_org_number; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone
    ADD CONSTRAINT uq_phone_org_number UNIQUE (organization_id, number);


--
-- Name: idx_building_location; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_building_location ON public.building USING gist (location);


--
-- Name: ix_building_location; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_building_location ON public.building USING gist (location);


--
-- Name: activity activity_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activity
    ADD CONSTRAINT activity_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES public.activity(id) ON DELETE CASCADE;


--
-- Name: organization_activity organization_activity_activity_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organization_activity
    ADD CONSTRAINT organization_activity_activity_id_fkey FOREIGN KEY (activity_id) REFERENCES public.activity(id) ON DELETE CASCADE;


--
-- Name: organization_activity organization_activity_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organization_activity
    ADD CONSTRAINT organization_activity_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.organization(id) ON DELETE CASCADE;


--
-- Name: organization organization_building_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_building_id_fkey FOREIGN KEY (building_id) REFERENCES public.building(id) ON DELETE RESTRICT;


--
-- Name: phone phone_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone
    ADD CONSTRAINT phone_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.organization(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

