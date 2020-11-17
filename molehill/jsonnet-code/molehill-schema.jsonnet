// Define the schema for molehill
local moo = import "moo.jsonnet";

local re_address = std.join('|',[moo.re.tcp, moo.re.ipc, moo.re.inproc]);

local mh = moo.oschema.schema("molehill");
local types = {
    ident: mh.string("Ident", pattern=moo.re.ident_only,
                    doc="An unique identifier"),

    cmdid: mh.enum("CmdId", symbols=[
        "undefined", "init", "conf", "start", "stop", "scrap", "term"
    ], doc="The canonical command name"),

    cmddata: mh.any("CmdData",
                doc="An opaque object holding command payload"),

    command: mh.record("Command", [
        mh.field("id", self.cmdid,
                 doc="Identify the type of command"),
        mh.field("name", self.ident,
                 doc="Uniquely identify this command"),
        // fixme: change to anyof([init, conf, ...])
        mh.field("data", self.cmddata, optional=true,
                 doc="Command data object with type-specific structure"),
    ], doc="Top-level command object structure"),
    commands: mh.sequence("Commands", self.command),

    cmdinit: mh.record("CmdInit", [
        mh.field("ident", self.ident,
                 doc="The name by which the node is known"),
        mh.field("role", self.ident,
                 doc="The role which this node will enact"),
        mh.field("ports", self.ports,
                 doc="Port socket descriptors"),
    ], doc="Init command structure"),

    cmdconf: mh.record("CmdConf", [
        mh.field("ident", self.ident,
                 doc="The name by which the node is known"),
    ], doc="Conf command structure"),

    // fixme: lift this to moo?
    socktype: mh.enum("SockType", symbols=[
        "pub","sub","pair"
    ], doc="Enumerate ZeroMQ socket types"),

    
    portaddr: mh.string("PortAddr",
                        pattern=re_address,
                        doc="Match legal ZeroMQ socket address schemes"),
    portaddrs: mh.sequence("PortAddrs", self.portaddr),

    port: mh.record("Port", [
        mh.field("name", self.ident, "Refer to this socket by a name"),
        mh.field("type", self.socktype, "Type of socket"),
        mh.field("binds", self.portaddrs, "Addresses to bind"),
        mh.field("conns", self.portaddrs, "Addresses to connect"),
    ], doc="Describe port socket"),
    ports: mh.sequence("Ports", self.port),

    slotspec: mh.string("SlotSpec", // fixme: figure our re matching rule lang
                       doc="A rule that matches against Slot records"),

    cmdline: mh.string("CmdLine", // fixme: some re
                       doc="A command line"),

    node: mh.record("Node", [
        mh.field("ident", self.ident,
                 doc="The name by which the node is known"),
        mh.field("role", self.ident,
                 doc="The role which this node will enact"),
        mh.field("slotspec", self.slotspec,
                 doc="Describe slot characteristics on which this node may run"),
        mh.field("ports", self.ports,
                 doc="Port socket descriptors"),
        mh.field("app", self.cmdline,
                 doc="The application command line to run"),
        mh.field("commands", self.commands,
                 doc="Commands that may be applied to node"),
    ], doc="Init command payload structure"),
    nodes: mh.sequence("Nodes", self.node),

    host: mh.string("Host", pattern=moo.re.dnshost),
    slot: mh.record("Slot", [
        mh.field("ident", self.ident,
                 doc="The name by which the slot is known"),
        mh.field("hostname", self.host,
                 doc="The DNS host name providing the slot"),
        mh.field("ipaddress", self.host,
                 doc="The IP address providing the slot"),
        mh.field("zone", self.ident,
                 doc="Some grouping of the slot"),
        // fixme: add more fields.  These are fodder for slotspec rules.
    ], doc="Describe a process slot"),
    slots: mh.sequence("Slots", self.slot),

    partnum: mh.number("Partition", "i4", // fixme: add constraint
                       doc="A small number counting the partition"),

    ssot: mh.record("SSOT", [
        mh.field("nodes", self.nodes, doc="Node info"),
        mh.field("slots", self.slots, doc="Slot info"),
        mh.field("partnum", self.partnum, default=0, doc="Partition number"),
    ], doc="Single source of truth object"),
};
moo.oschema.sort_select(types)
